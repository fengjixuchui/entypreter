DESCRIPTION = "Ignore ProtonScript runner exit."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    import time
    time.sleep(0)
