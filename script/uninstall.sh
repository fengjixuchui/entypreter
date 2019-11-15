#!/bin/bash

RS="\033[31m"
WHS="\033[0;97m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "\n(1/2) Uninstalling ProtonScript ..... [ FAIL ]\n"
   exit
fi


   sleep 1
   echo -e "\n(1/2) Uninstalling ProtonScript ..... [ OK ]"

{
rm /bin/pscript
rm /usr/local/bin/pscript
rm /data/data/com.termux/files/usr/bin/pscript
} &> /dev/null
sleep 5
echo -e ""
