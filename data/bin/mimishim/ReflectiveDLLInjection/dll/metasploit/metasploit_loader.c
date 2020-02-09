// Copyright (C) 2006-2010, Rapid7, Inc
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without modification,
// are permitted provided that the following conditions are met:
//
//     * Redistributions of source code must retain the above copyright notice,
//       this list of conditions and the following disclaimer.
//
//     * Redistributions in binary form must reproduce the above copyright notice,
//       this list of conditions and the following disclaimer in the documentation
//       and/or other materials provided with the distribution.
//
//     * Neither the name of Rapid7, Inc nor the names of its contributors
//       may be used to endorse or promote products derived from this software
//       without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
// ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
// ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
// SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//===============================================================================================//
#include "metasploit_loader.h"
//#include "metasploit_context.h"
#include "metasploit_ps.h"
//#include "metasploit_session.h"
#include "metasploit_inject.h"

#define VNCFLAG_DISABLECOURTESYSHELL		1
#define VNCFLAG_DISABLESESSIONTRACKING		2

//#include "../../ReflectiveDLLInjection/dll/src/ReflectiveLoader.c"

/*
* The HINSTANCE of this injected dll.
*/
extern HINSTANCE hAppInstance;

/*
* The socket created by stage one.
*/
SOCKET sock = INVALID_SOCKET;

/*
* Flag to disable following the active session as users log in an out of the input desktop.
*/
BOOL bDisableSessionTracking = FALSE;

/*
* The event that signals the remote client has closed the socket connection.
*/
HANDLE hSocketCloseEvent = NULL;

/*
* The event to terminate the vnc agent.
*/
HANDLE hAgentCloseEvent = NULL;

/*
* The process hosting the vnc agent.
*/
HANDLE hAgentProcess = NULL;

/*
* The rfb streams context we keep for the agent (see context.c)
*/
//extern AGENT_CTX AgentContext;

/*
* Extract the vnc.dll into the provided DLL_BUFFER.
*/
DWORD loader_vncdll(DLL_BUFFER * pDllBuffer)
{
	DWORD dwResult = ERROR_SUCCESS;
	HRSRC hVncResource = NULL;
	HGLOBAL hVncResourceLoad = NULL;
	LPVOID lpVncDllBuffer = NULL;
	DWORD dwVncDllSize = 0;
#ifdef _WIN64
	DWORD dwCompiledArch = PROCESS_ARCH_X64;
#else
	DWORD dwCompiledArch = PROCESS_ARCH_X86;
#endif

	do
	{
		if (!pDllBuffer)
			BREAK_WITH_ERROR("[LOADER] Init. pDllBuffer is null", ERROR_INVALID_PARAMETER);

		pDllBuffer->dwPE64DllLenght = 0;
		pDllBuffer->lpPE64DllBuffer = NULL;
		pDllBuffer->dwPE32DllLenght = 0;
		pDllBuffer->lpPE32DllBuffer = NULL;

		hVncResource = FindResource((HMODULE)hAppInstance, "IDR_VNC_DLL", "IMG");
		if (!hVncResource)
			BREAK_ON_ERROR("[LOADER] Init. FindResource failed");

		dwVncDllSize = SizeofResource((HMODULE)hAppInstance, hVncResource);
		if (!dwVncDllSize)
			BREAK_ON_ERROR("[LOADER] Init. SizeofResource failed");

		hVncResourceLoad = LoadResource((HMODULE)hAppInstance, hVncResource);
		if (!hVncResourceLoad)
			BREAK_ON_ERROR("[LOADER] Init. LoadResource failed");

		lpVncDllBuffer = LockResource(hVncResourceLoad);
		if (!lpVncDllBuffer)
			BREAK_ON_ERROR("[LOADER] Init. LockResource failed");

		dprintf("[LOADER] Init. lpVncDllBuffer=0x%08X, dwVncDllSize=%d", lpVncDllBuffer, dwVncDllSize);

		if (dwCompiledArch == PROCESS_ARCH_X64)
		{
			pDllBuffer->dwPE64DllLenght = dwVncDllSize;
			pDllBuffer->lpPE64DllBuffer = lpVncDllBuffer;
		}
		else if (dwCompiledArch == PROCESS_ARCH_X86)
		{
			pDllBuffer->dwPE32DllLenght = dwVncDllSize;
			pDllBuffer->lpPE32DllBuffer = lpVncDllBuffer;
		}

	} while (0);

	SetLastError(dwResult);

	return dwResult;
}

/*
* A pre injection hook called before our dll has been injected into a process.
*/
DWORD loader_inject_pre(DWORD dwPid, HANDLE hProcess, char * cpCommandLine)
{
	return ERROR_SUCCESS;
}

/*
* Close the various global handles we created for the agent..
*/
VOID loader_agent_close(VOID)
{
	CLOSE_HANDLE(hAgentCloseEvent);
	CLOSE_HANDLE(hAgentProcess);
}

/*
* A post injection hook called after our dll has been injected into a process.
*/
DWORD loader_inject_post(DWORD dwPid, HANDLE hProcess, DWORD dwInjectResult)
{
	return ERROR_SUCCESS;

}

/*
* Entry Point.
*/
DWORD Init(SOCKET s)
{
	return ERROR_SUCCESS;
}
