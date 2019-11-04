# The Entypreter Rootkit (TER)

             _                   _           
     ___ ___|||_ _ _ ___ ___ ___|||_ ___ ___ 
    | -_|   || _| | | . |  _| -_|| _| -_|  _|
    |___|_|_|_| |_  |  _|_| |___|_| |___|_|  
                |___|_|                      
             
<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a> 
  <a href="https://github.com/entynetproject/entypreter/releases">
    <img src="https://img.shields.io/github/release/entynetproject/entypreter.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/entypreter">
    <img src="https://img.shields.io/badge/implants-40-red.svg">
 </a>
  <a href="https://github.com/entynetproject/entypreter/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/entypreter.svg">
  </a>
  <a href="https://github.com/entynetproject/entypreter/wiki">
      <img src="https://img.shields.io/badge/wiki%20-entypreter-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About entypreter rootkit

    INFO: The Entypreter Rootkit is a Windows post exploitation rootkit similar to other penetration 
    testing tools such as Meterpreter and Powershell Invader Framework. The major difference is that The 
    Entypreter Rootkit does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), 
    with compatibility in the core to support a default installation of Windows 2000 with no service 
    packs (and potentially even versions of NT4) all the way through Windows 10.
   
***

# Getting started

## The entypreter installation

> cd entypreter

> chmod +x install.sh

> ./install.sh

## The entypreter uninstallation

> cd entypreter

> chmod +x uninstall.sh

> ./uninstall.sh

***

# How to execute entypreter

> entypreter -h

    usage: entypreter [-h] [--autorun AUTORUN] [--restore RESTORE] [-u]
                    
    optional arguments:
      -h, --help         show this help message and exit
      --autorun AUTORUN  A file containing Entypreter commands.
      --restore RESTORE  An Entypreter restore json file.
      -u, --update       Update The Entypreter Rootkit.
      
***

# The entypreter modules

    INFO: There are to kinds of The Entypreter Rootkit 
    modules - stagers and implants. Entypreter stagers 
    hook target session and allow you to use implants. 
    Entypreter implants starts jobs on remote session.
    
## The entypreter stagers

    INFO: Entypreter stagers hook target 
    session and allow you to use implants.

Module | Description
--------|------------
stager/js/mshta | Serves payloads using MSHTA.exe HTML Applications (default).
stager/js/regsvr | Serves payloads using regsvr32.exe COM+ scriptlets.
stager/js/wmic | Serves payloads using WMIC XSL.
stager/js/rundll32_js | Serves payloads using rundll32.exe.
stager/js/disk | Serves payloads using files on disk.

## The entypreter implants

    INFO: Entypreter implants starts 
    jobs on remote session.

Module | Description
--------|------------
implant/elevate/bypassuac_eventvwr | Uses enigma0x3's eventvwr.exe exploit to bypass UAC on Windows 7, 8, and 10.
implant/elevate/bypassuac_sdclt | Uses enigma0x3's sdclt.exe exploit to bypass UAC on Windows 10.
implant/fun/voice | Plays a message over text-to-speech.
implant/gather/clipboard | Retrieves the current content of the user clipboard.
implant/gather/enum_domain_info | Retrieve information about the Windows domain.
implant/gather/enum_printers | Retrieve information about printer connections.
implant/gather/hashdump_sam | Retrieves hashed passwords from the SAM hive.
implant/gather/hashdump_dc | Domain controller hashes from the NTDS.dit file.
implant/gather/user_hunter | Locate users logged on to domain computers.
implant/inject/mimikatz_dynwrapx | Injects a reflective-loaded DLL to run powerkatz.dll.
implant/inject/mimikatz_dotnet2js | Injects a reflective-loaded DLL to run powerkatz.dll.
implant/inject/shellcode_excel | Runs arbitrary shellcode payload (if Excel is installed).
implant/manage/enable_rdesktop | Enables remote desktop on the target.
implant/manage/exec_cmd | Run an arbitrary command on the target, and optionally receive the output.
implant/persist/add_user | Create a local/domain user.
implant/persist/registry | Add an Entypreter payload to the registry.
implant/persist/schtasks | Add an Entypreter payload as a Scheduled Task.
implant/persist/wmi | Add an Entypreter payload as a WMI subscription.
implant/phish/password_box | Prompt a user to enter their password.
implant/pivot/stage_wmi | Hook a session on another machine using WMI.
implant/pivot/exec_psexec | Run a command on another machine using psexec from sysinternals.
implant/util/download_file | Downloads a file from the target session.
implant/util/multi_module | Run a number of implants in succession.
implant/util/upload_file | Uploads a file from the listening server to the target sessions.

***

# TLS Communications

    INFO: To enable TLS communications, you will need 
    to host your Entypreter stager on a valid domain 
    (i.e. malicious.com) with a known Root CA signed 
    certificate. Windows will check its certificate 
    store and will NOT allow a self-signed certificate.
    
***
    
# Disclaimer

Usage of Entypreter for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, federal, and international laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    
***

# Entypreter apache license

    Copyright (C) 2016 - 2018 Entynetproject

    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use the software except in compliance with the License.

    You may obtain a copy of the License at:

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations under
    the License.

    Disclaimer:
    Usage of Entypreter for attacking targets without prior mutual consent is illegal.
    It is the end user's responsibility to obey all applicable local, state,
    federal, and international laws. Developers assume no liability and are not
    responsible for any misuse or damage caused by this program.
    
***

# Thats all!
