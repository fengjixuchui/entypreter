DESCRIPTION = "Clear terminal window."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    import os
    os.system("clear")
