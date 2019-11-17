# ProtonScript (Proton Language)

                                _____         _           _____         _     _   
                               |  _  |___ ___| |_ ___ ___|   __|___ ___|_|___| |_ 
                               |   __|  _| . |  _| . |   |__   |  _|  _| | . |  _|
                               |__|  |_| |___|_| |___|_|_|_____|___|_| |_|  _|_|  
                                                                         |_|  
***

![pscode](https://user-images.githubusercontent.com/54115104/68995309-36c52980-089d-11ea-8852-f89ff5b07a17.png)

# About ProtonScript

    INFO: ProtonScript is a Proton Framework programming language
    used to quickly execute Proton commands in the Proton Framework, 
    you can install the ProtonScript via the Proton Framework.
    
***

# Getting started

## ProtonScript installation

> cd proton/script

> chmod +x install.sh

> ./install.sh

## ProtonScript uninstallation

> cd proton/script

> chmod +x uninstall.sh

> ./uninstall.sh

***

# How to execute ProtonScript

> pscript -h

```
usage: pscript [-h] [-v] [-n] [-u] [--no-output OPTION] 
                                   [-e FILE] [-d FILE]
                                   
optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Display ProtonScript version.
  -n, --notepad         Open the ProtonScript notepad.
  -u, --update          Update the ProtonScript.
  --no--output OPTION   
                        Disable ProtonScript output.
  -e FILE, --encode FILE
                        Encode a ProtonScript program.
  -d FILE, --decode FILE 
                        Decode a ProtonScript program.
```

***

# Writing ProtonScript program

    INFO: So, we are going to write 
    our first ProtonScript program.
    
**1.** Write ProtonScript program in the ProtonScript notepad.    
    
> pscript -n

![psnotepad](https://user-images.githubusercontent.com/54115104/68992304-ab3aa100-087a-11ea-8acb-4402ffbb6fcd.png)

**2.** Copy this code to a file, name it `program.p`.

**3.** Encode your ProtonScript program file via `pscript`.

> pscript -e program.p

```
(1/4) Loading Program File  ..... [ OK ]
(2/4) Loading ProtonScript  ..... [ OK ]
(3/4) Encoding Program File ..... [ OK ]
(4/4) Saving Program File   ..... [ OK ]
```

***

# Running ProtonScript program

> proton -r program.bin

```
(1/3) Loading Program File  ..... [ OK ]
(2/3) Loading ProtonScript  ..... [ OK ]
(3/3) Running Program File  ..... [ OK ]
```

![Hello, World!](https://user-images.githubusercontent.com/54115104/69009133-ac93c880-0963-11ea-8361-9eb8492a7bd1.png)

***

# Decoding ProtonScript program

> pscript -d program.bin

```
(1/4) Loading Program File  ..... [ OK ]
(2/4) Loading ProtonScript  ..... [ OK ]
(3/4) Decoding Program File ..... [ OK ]
(4/4) Saving Program File   ..... [ OK ]
```

***

# ProtonScript commands

    COMMAND     DESCRIPTION     
    ---------   -------------   
    API         Turn on/off the rest API.
    BACK        Go back to the last used module.
    CLEAR       Clear terminal window.
    CREDS       Show collected credentials.
    DELAY       Proton Framework delay in seconds.
    DOMAIN      Show collected domain information.
    EDIT        Edit the current module.
    EXIT        Exit from the Proton Framework.
    HELP        Display help info for a command.
    INFO        Display the current module options.
    JOBS        Display info about jobs.
    KILL        Kill a zombie or all zombies.
    LOAD        Reload all Proton Framework modules.
    LOGO        Proton Framework logo.
    NOPSE       Ignore ProtonScript runner exit.
    PRINT       Print some text.
    PYEXEC      Eval some python code.
    REPEAT      Display info about repeating job.
    RUN         Run the current module.
    SET         Set a variable for the current module.
    SHELL       Open zombie's CMD shell.
    SOUNDS      Turn sounds on/off.
    SPOOL       Write output to a file.
    STAGERS     Display info about stagers.
    UNSET       Unset a variable for the current module.
    USE         Switch to a different module.
    VERBOSE     Turn verbosity on/off.
    ZOMBIES     List hooked zombies.
    
***

# ProtonScript license

```
    --------------------------------------------------
                       ProtonScript          
    --------------------------------------------------
  Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.                
```
    
# Thats all!
