# Proton Framework (Remote Command & Control)

                                                           _           
                                               ___ ___ ___| |_ ___ ___ 
                                              | . |  _| . |  _| . |   |
                                              |  _|_| |___|_| |___|_|_|
                                              |_|                      

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a> 
  <a href="https://github.com/entynetproject/proton/releases">
    <img src="https://img.shields.io/github/release/entynetproject/proton.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/proton">
    <img src="https://img.shields.io/badge/implants-44-red.svg">
 </a>
  <a href="https://github.com/entynetproject/proton/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/proton.svg">
  </a>
  <a href="https://github.com/entynetproject/proton/wiki">
      <img src="https://img.shields.io/badge/wiki%20-proton-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

![proton](https://user-images.githubusercontent.com/54115104/69095595-b3096980-0a63-11ea-89ee-97ac47f64d32.png)

# About proton framework

    INFO: Proton Framework is a Windows post exploitation framework similar to other penetration 
    testing tools such as Meterpreter and Powershell Invader Framework. The major difference is that 
    the Proton Framework does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), 
    with compatibility in the core to support a default installation of Windows 2000 with no service 
    packs (and potentially even versions of NT4) all the way through Windows 10.
   
***

# Getting started

## Proton installation

> cd proton

> chmod +x install.sh

> ./install.sh

## Proton uninstallation

> cd proton

> chmod +x uninstall.sh

> ./uninstall.sh

***

# How to execute proton

> proton -h

```
usage: proton [-h] [-r FILE] [-j FILE] [-u]

optional arguments:
  -h, --help            show this help message and exit
  -i, --install         Install the ProtonScript.
  -r FILE, --run FILE
                        Run a ProtonScript program.
  -j FILE, --json FILE
                        A Proton Framework json file.
  -u, --update          Update Proton Framework.
```
      
***

# Proton framework modules

![modules](https://user-images.githubusercontent.com/54115104/69085038-71be8d00-0a56-11ea-809c-f4e4ca6707b4.png)

    INFO: There are to kinds of Proton Framework 
    modules - stagers and implants. Proton stagers hook 
    target zombies and allow you to use implants. Proton 
    implants starts jobs on remote target zombie.
    
## Proton stagers

    INFO: Proton stagers hook target 
    zombie and allow you to use implants.

Name | Description
--------|------------
mshta | Serves payloads using MSHTA.exe HTML Applications (default).
regsvr | Serves payloads using regsvr32.exe COM+ scriptlets.
wmic | Serves payloads using WMIC XSL.
rundll32_js | Serves payloads using rundll32.exe.
disk | Serves payloads using files on disk.
bitsadmin | Transfers a .wsf payload containing JScript over a Bitsadmin job and executes it.

## Proton implants

    INFO: Proton implants starts 
    jobs on a remote zombie target.

Name | Description
--------|------------
bypassuac_compdefaults | Bypass UAC via registry hijack for ComputerDefaults.exe.
bypassuac_compmgmtlauncher | Bypass UAC via registry hijack for CompMgmtLauncher.exe.
bypassuac_eventvwr | Uses eventvwr.exe exploit to bypass UAC on Windows 7, 8, and 10.
bypassuac_fodhelper | Bypass UAC via registry hijack for fodhelper.exe.
bypassuac_sdclt | Uses sdclt.exe exploit to bypass UAC on Windows 10.
bypassuac_slui | Bypass UAC via registry hijack for slui.exe.
system_createservice | Elevate from administrative session to SYSTEM via SC.exe.
youtube | Maxes volume and opens the specified YouTube video in a hidden window.
voice | Plays a message over text-to-speech.
clipboard | Retrieves the current content of the user clipboard.
comsvcs_lsass | Utilizes comsvcs.dll to create a MiniDump of LSASS, parses with pypykatz.
enum_domain_info | Retrieve information about the Windows domain.
hashdump_dc | Domain controller hashes from the NTDS.dit file.
hashdump_sam | Retrieves hashed passwords from the SAM hive.
loot_finder | Finds loot on the target box.
user_hunter | Locate users logged on to domain computers (using Dynamic Wrapper X).
mimikatz_dotnet2js | Injects a reflective-loaded DLL to run powerkatz.dll.
mimikatz_dynwrapx | Injects a reflective-loaded DLL to run powerkatz.dll (using Dynamic Wrapper X).
mimikatz_tashlib | Executes arbitrary shellcode using the TashLib COM object.
shellcode_dotnet2js | Executes arbitrary shellcode using the DotNet2JS technique. Inject shellcode into a host process via createremotethread as a new thread.
shellcode_dynwrapx | Executes arbitrary shellcode using the Dynamic Wrapper X COM object.
shellcode_excel | Runs arbitrary shellcode payload (if Excel is installed).
enable_rdesktop | Enables remote desktop on the target.
exec_cmd | Run an arbitrary command on the target, and optionally receive the output.
add_user | Adds a either a local or domain user.
registry | Adds a Proton stager payload in the registry.
schtasks | Establishes persistence via a scheduled task.
wmi | Creates persistence using a WMI subscription.
password_box | Prompt a user to enter their password.
exec_psexec | Run a command on another machine using psexec from sysinternals.
exec_wmi | Executes a command on another system.
stage_wmi | Hook a zombie on another machine using WMI.
tcp | Uses HTTP to scan open TCP ports on the target zombie LAN.
download_file | Downloads a file from the target zombie.
multi_module | Run a number of implants in succession.
upload_file | Uploads a file from the listening server to the target zombies.

***

# TLS communications

    INFO: To enable TLS communications, you will need 
    to host your Proton stager on a valid domain 
    (i.e. malicious.com) with a known Root CA signed 
    certificate. Windows will check its certificate 
    store and will NOT allow a self-signed certificate.
    
***

# ProtonScript (Proton Language)

![pscode](https://user-images.githubusercontent.com/54115104/68995309-36c52980-089d-11ea-8852-f89ff5b07a17.png)

    INFO: ProtonScript is a Proton Framework programming language
    used to quickly execute Proton commands in the Proton Framework, 
    you can install the ProtonScript via the Proton Framework.
    
> proton -i

    (1/1) Installing ProtonScript ..... [ OK ]
    
# ProtonScript documentation

    INFO: You can read more about ProtonScript from the 
    ProtonScript documentation. You can find the ProtonScript 
    documentation in the Proton Framework script directory. 
   
***
    
# Disclaimer

    Usage of Proton for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    
***

# Proton apache license

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
    Usage of the Proton Framework for attacking targets without prior mutual consent 
    is illegal. It is the end user's responsibility to obey all applicable local, 
    state, federal, and international laws. Developers assume no liability and 
    are not responsible for any misuse or damage caused by this program.
    
***

# Thats all!
