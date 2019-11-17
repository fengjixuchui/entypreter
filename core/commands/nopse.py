DESCRIPTION = "Ignore ProtonScript runner exit."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    os.system("printf '\033]2;Proton Framework\a'")
    import time
    time.sleep(0)
