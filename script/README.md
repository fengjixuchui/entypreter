# ProtonScript (Proton Language)

                                _____         _           _____         _     _   
                               |  _  |___ ___| |_ ___ ___|   __|___ ___|_|___| |_ 
                               |   __|  _| . |  _| . |   |__   |  _|  _| | . |  _|
                               |__|  |_| |___|_| |___|_|_|_____|___|_| |_|  _|_|  
                                                                         |_|  

![pscript](https://user-images.githubusercontent.com/54115104/69556144-505d2400-0fb5-11ea-8184-108f3c1c852c.png)

***

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

![Hello, World!](https://user-images.githubusercontent.com/54115104/69556145-50f5ba80-0fb5-11ea-87c7-cc1a0c024448.png)

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

![runner](https://user-images.githubusercontent.com/54115104/69009297-12cd1b00-0965-11ea-8963-5e229003bfbf.png)

## Using proton command

> proton -r program.psc

```
(1/3) Loading Program File  ..... [ OK ]
(2/3) Loading ProtonScript  ..... [ OK ]
(3/3) Running Program File  ..... [ OK ]
```

## Using ProtonScript environment

    INFO: ProtonScript environment is a feature that 
    allows you to run ProtonScript program without 
    encoding and without using a proton command.

**1.** Add a `#!/usr/bin/env psenv` hasbang to your ProtonScript program file.

**2.** Run `program.p` using this following commands.

> chmod +x program.p

> ./program.p

```
(1/3) Loading Program File  ..... [ OK ]
(2/3) Loading ProtonScript  ..... [ OK ]
(3/3) Running Program File  ..... [ OK ]
```

***

# Decoding ProtonScript program

> pscript -d program.psc

```
(1/4) Loading Program File  ..... [ OK ]
(2/4) Loading ProtonScript  ..... [ OK ]
(3/4) Decoding Program File ..... [ OK ]
(4/4) Saving Program File   ..... [ OK ]
```

***

# ProtonScript commands

    COMMAND     DESCRIPTION     
    -------     -----------   
    api         Turn on/off the rest API.
    back        Go back to the last used module.
    clear       Clear terminal window.
    creds       Show collected credentials.
    delay       Proton Framework delay in seconds.
    domain      Show collected domain information.
    edit        Edit the current module.
    exit        Exit from the Proton Framework.
    help        Display help info for a command.
    info        Display the current module options.
    jobs        Display info about jobs.
    kill        Kill a zombie or all zombies.
    load        Reload all Proton Framework modules.
    logo        Display Proton Framework logo.
    modules     Display all stagers or all implants.
    nopse       Ignore ProtonScript runner exit.
    print       Print some text.
    pyexec      Eval some python code.
    repeat      Display info about repeating job.
    run         Run the current module.
    set         Set a variable for the current module.
    shell       Open zombie's CMD shell.
    sounds      Turn sounds on/off.
    spool       Write output to a file.
    stagers     Display info about stagers.
    unset       Unset a variable for the current module.
    use         Switch to a different module.
    verbose     Turn verbosity on/off.
    zombies     List hooked zombies.
    
***

# ProtonScript license

```
    --------------------------------------------------
                       ProtonScript          
    --------------------------------------------------
          Copyright (C) <2019>  <Entynetproject>

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

***
    
# Thats all!
