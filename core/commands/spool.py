import os

DESCRIPTION = "Write output to a file."

def autocomplete(shell, line, text, state):
    options = filepaths(text)
    return options[state]

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "spool on" to turn spooling on and spool to /tmp/entypreter.spool.')
    shell.print_plain('Use "spool %s" to turn spooling on and spool to the specified file.' % (shell.colors.colorize("FILEPATH", shell.colors.BOLD)))
    shell.print_plain('Use "spool off" to turn spooling off and save spool file.')
    shell.print_plain("")

def filepaths(text):
    import readline
    everything = readline.get_line_buffer()
    cursor_idx = readline.get_begidx()
    idx = 0
    for chunk in everything.split(" "):
        fullpath = chunk
        idx += len(chunk) + 1
        if idx > cursor_idx:
            break

    if os.path.isfile(fullpath):
        return None
    if "/" in fullpath:
        d = os.path.dirname(fullpath)
    else:
        d = "."

    res = []
    for candidate in os.listdir(d):
        if not candidate.startswith(text):
            continue
        if os.path.isdir(d+os.path.sep+candidate):
            res.append(candidate + os.path.sep)
        else:
            res.append(candidate + " ")
    return res

def execute(shell, cmd):

    splitted = cmd.split()

    if len(splitted) > 1:
        option = splitted[1]
        if option == 'on':
            shell.spool = '/tmp/entypreter.spool'
            shell.spoolstatus = True
            shell.print_status("Spooling: %s" % ("on" if shell.spoolstatus else "off"))
            shell.print_status("Spooling to /tmp/entypreter.spool...")
        elif option == 'off':
            if shell.spool:
                shell.spoolstatus = False
                shell.print_status("Spooling: %s" % ("on" if shell.spoolstatus else "off"))
        else:
            shell.spool = option
            shell.spoolstatus = True
            shell.print_status("Spooling: %s" % ("on" if shell.spoolstatus else "off"))
            shell.print_status("Spooling to "+option+"...")
    else:
        help(shell)
