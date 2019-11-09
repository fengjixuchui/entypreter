#!/bin/bash

# Copyright (C) 2016 - 2018 Entynetproject
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
#
# Disclaimer:
# Usage of the Proton Framework for attacking targets without prior mutual consent 
# is illegal. It is the end user's responsibility to obey all applicable local, 
# state, federal, and international laws. Developers assume no liability and 
# are not responsible for any misuse or damage caused by this program.

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RS"*"$CE"] "$RS"This script must be run as "$YS"root"$C"" 1>&2
   sleep 1
   exit
fi

{
rm /bin/proton
rm /usr/local/bin/proton
rm -r ~/proton
rm /etc/proton.conf
rm /data/data/com.termux/files/usr/bin/proton
} &> /dev/null
