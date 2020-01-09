DESCRIPTION = "Update Proton Framework."

def autocomplete(shell, line, text, state):
    pass

def help(shell):
    pass

def execute(shell, cmd):
    import os
    os.system("chmod +x etc/update.sh && etc/update.sh")
