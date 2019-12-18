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

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[31m"
#green start
	GNS="-e \033[1;32m"
#white start
   WHS="\033[0;97m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-] "$WHS"This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/proton ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/proton.git
} &> /dev/null
fi
sleep 0.5
clear
sleep 0.5
cd ~/proton
echo -e """                       _           
           ___ ___ \033[32m___\033[0m| |_ \033[32m___ \033[0m___ 
          | . |  _\033[32m| . |\033[0m  _\033[32m| . |\033[0m   |
          |  _|_| \033[32m|___|\033[0m_| \033[32m|___|\033[0m_|_|
          |_|                      """
echo

sleep 1
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install python
apt-get -y install python3
apt-get -y install python3-pip
apk update
apk add python3
apk add py3-pip
pacman -Sy
pacman -S --noconfirm python3
pacman -S --noconfirm python3-pip
zypper refresh
zypper install -y python3
zypper install -y python3-pip
yum -y install python3
yum -y install python3-pip
dnf -y install python3
dnf -y install python3-pip
eopkg update-repo
eopkg -y install python3
eopkg -y install pip
xbps-install -S
xbps-install -y python3
xbps-install -y python3-pip
} &> /dev/null

{
pip3 install -r requirements.txt
} &> /dev/null

{
cd ~/proton/bin
cp proton /usr/local/bin
chmod +x /usr/local/bin/proton
cp proton /bin
chmod +x /bin/proton
cp proton /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/proton
} &> /dev/null
