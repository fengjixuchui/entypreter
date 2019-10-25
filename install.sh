#! /bin/bash

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
# Usage of Entypreter for attacking targets without prior mutual consent is illegal.
# It is the end user's responsibility to obey all applicable local, state,
# federal, and international laws. Developers assume no liability and are not
# responsible for any misuse or damage caused by this program.

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[31m"
#green start
	GNS="-e \033[32m"
#white start
   WHS="\033[0;97m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RS"*"$CE"] "$RS"This script must be run as "$YS"root"$C"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/entypreter ]]
then
cd ~/entypreter/bin
{
cp entypreter /usr/local/bin
chmod +x /usr/local/bin/entypreter
cp entypreter /bin
chmod +x /bin/entypreter
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/entypreter.git
cd ~/entypreter/bin
cp entypreter /usr/local/bin
chmod +x /usr/local/bin/entypreter
cp entypreter /bin
chmod +x /bin/entypreter
} &> /dev/null
fi
sleep 0.5
clear
sleep 0.5
echo
echo -e "            \033[1;32m _  \033[0m                \033[1;32m _ \033[0m"       
echo -e "     ___ ___\033[1;32m|||_\033[0m _ _ ___ ___ ___\033[1;32m|||_\033[0m ___ ___"
echo -e "    | -_|   \033[1;32m|| _|\033[0m | | . |  _| -_\033[1;32m|| _|\033[0m -_|  _|"
echo -e "    |___|_|_\033[1;32m|_| \033[0m|_  |  _|_| |___\033[1;32m|_| \033[0m|___|_|"
echo -e "                |___|_|"        
echo

if [[ -f /etc/entypreter.conf ]]
then

CONF="$( cat /etc/entypreter.conf )"
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
pkg update
pkg -y install python3
pkg -y install python3-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
fi
fi

else
read -e -p $'\033[1;34m[*]\033[0;97m Select your architecture (amd/intel/arm): \033[0m' CONF
if [[ "$CONF" = "" ]]
then
exit
else
if [[ "$CONF" = "arm" ]]
then
read -e -p $'\033[1;34m[*]\033[0;97m Is this a single board computer (yes/no): \033[0m' PI
if [[ "$PI" = "yes" ]]
then
echo "amd" >> /etc/entypreter.conf
CONF="amd"
else
echo "$CONF" >> /etc/entypreter.conf
fi
fi
fi
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
pkg update
pkg -y install python3
pkg -y install python3-pip
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
else 
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
fi
fi
fi

{
pip3 install setuptools
pip3 install -r requirements.txt
} &> /dev/null
