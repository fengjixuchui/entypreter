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

{
rm /bin/pscript
rm /usr/local/bin/pscript
rm /data/data/com.termux/files/usr/bin/pscript
} &> /dev/null
