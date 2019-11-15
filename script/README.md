# ProtonScript (Proton Language)

                                _____         _           _____         _     _   
                               |  _  |___ ___| |_ ___ ___|   __|___ ___|_|___| |_ 
                               |   __|  _| . |  _| . |   |__   |  _|  _| | . |  _|
                               |__|  |_| |___|_| |___|_|_|_____|___|_| |_|  _|_|  
                                                                         |_|  
***

# About ProtonScript

    INFO: ProtonScript is a Proton Framework programming language
    used to quickly execute Proton commands in the Proton Framework, 
    you can enable the ProtonScript feature via Proton Framework.
    
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

```ruby
#include <psio>

USE disk #using disk stager
SET SRVHOST host #setting up a server host
SET SRVPORT port #setting up a server port
RUN #executing disk stager
```

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

# Executing ProtonScript program

> proton -p program.bin

```
(1/3) Loading Program File  ..... [ OK ]
(2/3) Loading ProtonScript  ..... [ OK ]
(3/3) Running Program File  ..... [ OK ]
```

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
    
# Thats all!
