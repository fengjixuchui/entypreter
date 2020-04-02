#!/usr/bin/env python3

#            ---------------------------------------------------
#                             Proton Framework              
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time

DESCRIPTION = "Exit Proton Framework."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def convert_to_parsable(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for key in obj:
            if isinstance(key, tuple):
                new_obj['/'.join(key)] = obj[key]
            elif isinstance(key, str):
                new_obj[key] = obj[key]

    elif isinstance(obj, list):
        new_obj = []
        for val in obj:
            if isinstance(val, tuple):
                new_obj.append('/'.join(val))
            elif isinstance(val, str):
                new_obj.append(val)
    else:
        new_obj = []

    return new_obj

def execute(shell, cmd):
    import sys
    sys.exit(0)
