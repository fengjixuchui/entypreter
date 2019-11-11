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

# How to execute ProtonScript

> pscript -h

```
usage: pscript [-h] [-v] [-g] [--no-output OPTION] 
                              [-e FILE] [-d FILE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Display ProtonScript version.
  -g, --gui             Open a ProtonScript GUI console.

ProtonScript Coder:
  --no--output OPTION   
                        Disable ProtonScript Coder output.
  -e FILE, --encode FILE
                        Encode a ProtonScript program file.
  -d FILE, --decode FILE 
                        Decode a ProtonScript program file."""
```

***

# Writing ProtonScript program

    INFO: So, we are going to write 
    our first ProtonScript program.

## Writing program

    INFO: There is the ProtonScript GUI console 
    for the comfortable writing a code with colors.
    
> pscript -g

**1.** Write ProtonScript code in the ProtonScript GUI console using this option.

```ruby
#include <psio>

USE disk #using disk stager
SET SRVHOST host #setting up a server host
SET SRVPORT port #setting up a server port
RUN #executing disk stager
```

**2.** Save this ProtonScript code as `program.p`.

## Encoding program

> pscript -e program.p

```
ProtonScript Coder v3.0

(1/4) Loading Program File  ..... [ OK ]
(2/4) Loading ProtonScript  ..... [ OK ]
(3/4) Encoding Program File ..... [ OK ]
(4/4) Saving Program File   ..... [ OK ]

```

## Executing program

> proton -p program.p

```
ProtonScript Coder v3.0

(1/3) Loading Program File  ..... [ OK ]
(2/3) Loading ProtonScript  ..... [ OK ]
(3/3) Running Program File  ..... [ OK ]

```

## Decoding program

```
ProtonScript Coder v3.0

(1/4) Loading Program File  ..... [ OK ]
(2/4) Loading ProtonScript  ..... [ OK ]
(3/4) Decoding Program File ..... [ OK ]
(4/4) Saving Program File   ..... [ OK ]
```

***
    
# Thats all!
