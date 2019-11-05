DESCRIPTION = "Turn verbosity on/off."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain("Usage: verbose [on|off]")
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()

    if len(splitted) > 1:
        sw = splitted[1].lower()
        if sw == "1" or sw == "true" or sw == "on":
            shell.verbose = True
            shell.print_status("Verbosity: %s" % ("on" if shell.verbose else "off"))
        if sw == "0" or sw == "false" or sw == "off":
            shell.verbose = False
            shell.print_status("Verbosity: %s" % ("on" if shell.verbose else "off"))
    else:
        help(shell)
