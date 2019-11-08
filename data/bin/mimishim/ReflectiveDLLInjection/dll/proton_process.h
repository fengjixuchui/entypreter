#pragma once

#include <Windows.h>

#include "proton_types.h"

#define MIMISHIM_X64_OFFSET 7620


BOOL proton_create_sysnative_process(LPCSTR program, LPDWORD dwPID);
BOOL proton_fork_x64(proton_shim_parsed *parsed, LPWSTR lpParam, char *data, DWORD dwDataSize);
