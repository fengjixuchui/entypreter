#!/bin/bash

# Copyright (C) 2016 - 2019 Entynetproject
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use the software except in compliance with the License.
#
# You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

WHS="\033[0;97m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-] "$WHS"This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

{
rm /bin/proton
rm /usr/local/bin/proton
rm -rf ~/proton
rm /etc/proton.conf
rm /data/data/com.termux/files/usr/bin/proton
rm /bin/pscript
rm /usr/local/bin/pscript
rm /data/data/com.termux/files/usr/bin/pscript
rm /bin/psenv
rm /usr/local/bin/psenv
rm /data/data/com.termux/files/usr/bin/psenv
rm /usr/share/nano/pscript.nanorc
rm /usr/local/share/nano/pscript.nanorc
} &> /dev/null
