import time

DESCRIPTION = "Proton Framework delay in seconds."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "delay %s" to delay the Proton Framework.' % (shell.colors.colorize("SECONDS", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()
    
    if len(splitted) > 1:
        seconds = " ".join(cmd.split(" ")[1:])
        time.sleep(float(seconds))
    else:
        help(shell)
