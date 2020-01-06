#!/bin/bash

#            --------------------------------------------------
#                             Proton Framework              
#            --------------------------------------------------
#                  Copyright (C) <2019>  <Entynetproject>
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

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

printf '\033]2;uninstall.sh\a'

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
