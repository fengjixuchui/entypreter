#!/bin/bash

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

printf '\033]2;install.sh\a'

G="\033[1;34m[*] \033[0m"
S="\033[1;32m[+] \033[0m"
E="\033[1;31m[-] \033[0m"

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then 
   echo -e ""$E"No Internet connection!"
   exit
fi

sleep 0.5
clear
sleep 0.5
echo -e """              _           
  ___ ___ \033[32m___\033[0m| |_ \033[32m___ \033[0m___ 
 | . |  _\033[32m| . |\033[0m  _\033[32m| . |\033[0m   |
 |  _|_| \033[32m|___|\033[0m_| \033[32m|___|\033[0m_|_|
 |_|                      """
echo

sleep 1
echo -e ""$G"Installing dependencies..."
sleep 1

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python3
brew install git
curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py
sudo python3 /tmp/get-pip.py

if [[ -d ~/proton ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/proton.git
} &> /dev/null
fi

if [[ -d ~/proton ]]
then
cd ~/proton
else
echo -e ""$E"Installation failed!"
exit
fi

{
sudo python3 -m pip install setuptools
sudo python3 -m pip install -r requirements.txt
} &> /dev/null

{
cd bin
sudo cp proton /usr/local/bin
sudo chmod +x /usr/local/bin/proton
sudo cp proton /bin
sudo chmod +x /bin/proton
sudo cp proton /data/data/com.termux/files/usr/bin
sudo chmod +x /data/data/com.termux/files/usr/bin/proton
} &> /dev/null

sleep 1
echo -e ""$S"Successfully installed!"
sleep 1
