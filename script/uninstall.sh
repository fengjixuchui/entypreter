#!/bin/bash

# 
#            --------------------------------------------------
#                               ProtonScript               
#            --------------------------------------------------
#          Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>
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
#
#
#    About Author :   
#    Founder   : Entynetproject (Ivan Nikolsky)
#    Site      : http://entynetproject.simplesite.com/
#    Instagram : @entynetproject 
#    Twitter   : @entynetproject
#    Email     : entynetproject@gmail.com
#

RS="\033[31m"
WHS="\033[0;97m"
CE="\033[0m"
G="\033[1m"
R="\033[1m"
E="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "\n(1/1) Uninstalling ProtonScript ..... [ "$R"FAIL"$E" ]\n"
   exit
fi


   sleep 1
   echo -e "\n(1/1) Uninstalling ProtonScript ..... [ "$G"OK"$E" ]"

{
rm /bin/pscript
rm /usr/local/bin/pscript
rm /data/data/com.termux/files/usr/bin/pscript
} &> /dev/null
sleep 5
echo -e ""
