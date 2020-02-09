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

import sys

syskey_data_file = sys.argv[1]

tmp_syskey = ""
syskey = ""
with open(syskey_data_file, 'rb') as syskeyfile:
    file_contents = syskeyfile.read()

i = 4220
while i < 28811:
    j = i + 15
    while i < j:
        tmp_syskey += file_contents[i:i+1].decode()
        i += 2
    i += 8176

tmp_syskey = list(map(''.join, zip(*[iter(tmp_syskey)]*2)))

transforms = [8, 5, 4, 2, 11, 9, 13, 3, 0, 6, 1, 12, 14, 10, 15, 7]
for i in transforms:
    syskey += tmp_syskey[i]

print("Decoded SysKey: 0x%s" % syskey)
