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

#include <Windows.h>

// strcpy 4 life-- it was a buffalo overflow, in the heart of the shellcode
#if (_MSC_VER >= 1400)         // Check MSC version
#pragma warning(disable: 4996) // Disable deprecation
#endif

#pragma pack(push, 1)

typedef struct _proton_shim_parsed {
	CHAR host[512];
	CHAR path[512];
	WORD port;
	BOOL secure;
	CHAR uuidHeader[100];
	CHAR uuidMimix86[40];
	CHAR uuidMimix64[40];
	CHAR uuidShimx64[40];
	CHAR mimicmd[100]; // 'twas a buffalo overflow
} proton_shim_parsed;

#pragma pack(pop)
