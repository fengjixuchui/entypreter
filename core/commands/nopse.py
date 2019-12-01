DESCRIPTION = "Ignore ProtonScript runner exit."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    import os
    import os.path
    if (os.path.exists("/data/data/com.termux")):
        pspath = "/data/data/com.termux/files/usr/bin/pscript"
    else:
        pspath = "/usr/local/bin/pscript"

    if (os.path.exists(pspath)):
        import time
        time.sleep(0)
    else:
        RS = "\033[1;31m"
        WS = "\033[0;97m"
        CE = "\033[0m"
        print(RS+"[-]"+WS+" ProtonScript is not installed!"+CE)
        pass

    import time
    time.sleep(0)
