DESCRIPTION = "Turn verbosity on/off: verbose (on|off)."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    splitted = cmd.split()

    if len(splitted) > 1:
        sw = splitted[1].lower()
        if sw == "1" or sw == "true" or sw == "on":
            shell.verbose = True
        else:
            shell.verbose = False

    shell.print_status("Verbosity: %s" % ("on" if shell.verbose else "off"))
