#!/bin/bash

RS="\033[31m"
WHS="\033[0;97m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-] "$WHS"This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

if -d ~/proton; then
  sleep 0
else
  cd ~
  {
  git clone https://github.com/entynetproject/proton.git
  } &> /dev/null
  cd ~/proton
  chmod +x install.sh
  ./install.sh
fi

{
cd ~/proton/script/bin
cp pscript /usr/local/bin
chmod +x /usr/local/bin/pscript
cp pscript /bin
chmod +x /bin/proton
cp pscript /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/pscript
} &> /dev/null
  
