#pragma once

#include <Windows.h>

#include "proton_types.h"

BOOL proton_get_debug_priv();
BOOL proton_cpu_matches_process();

// proposed buffalo format:
// UUIDHEADER~~UUIDSHIMX64~~UUIDMIMIKATZX86~~UUIDMIMIKATZ64~~WORKURL
BOOL proton_parse_shim(LPWSTR buffalo, proton_shim_parsed *parsed);