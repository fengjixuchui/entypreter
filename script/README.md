# ProtonScript (Proton Language)

                                _____         _           _____         _     _   
                               |  _  |___ ___| |_ ___ ___|   __|___ ___|_|___| |_ 
                               |   __|  _| . |  _| . |   |__   |  _|  _| | . |  _|
                               |__|  |_| |___|_| |___|_|_|_____|___|_| |_|  _|_|  
                                                                         |_|  
***

# About ProtonScript

    INFO: ProtonScript is a Proton Framework programming language
    used to quickly execute Proton commands in the Proton Framework.
   
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

# How to execute pscript

> pscript -h

```
usage: pscript [-h] [-w FILE] [-e FILE] [-d FILE]

optional arguments:
  -h, --help            show this help message and exit
  -w FILE, --write FILE 
                        Write a ProtonScript program.
  -e FILE, --encode FILE
                        Encode a ProtonScript program file.
  -d FILE, --decode FILE 
                        Decode a ProtonScript program file.
```

***

# Writing ProtonScript program

    INFO: So, we are going to write 
    our first ProtonScript program.

## Writing program
    
> pscript -w program.p

```ruby
#include <psio>

USE disk #using disk stager
SET SRVHOST host #setting up a server host
SET SRVPORT port #setting up a server port
RUN #executing disk stager
```

## Encoding program

> pscript -e program.p

```
ProtonScript Coder 3.0


```

***
    
# Thats all!
