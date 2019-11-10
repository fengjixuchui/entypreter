# ProtonScript (Proton Commands)

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

# Writing ProtonScript program

    INFO: So, we are going to write 
    our first ProtonScript program.
    
> pscript main.p

```ruby
#include <psio>

USE disk #using disk stager
SET SRVHOST host #setting up a server host
SET SRVPORT port #setting up a server port
RUN #executing disk stager
```

> pscript -c main.p

> proton -p main.p

***
    
# Thats all!
