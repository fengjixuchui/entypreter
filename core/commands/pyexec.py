DESCRIPTION = "Eval some python code."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "pyexec %s" to eval the specified python code.' % (shell.colors.colorize("CODE", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()
    
    if len(splitted) > 1:
        code = " ".join(cmd.split(" ")[1:])
        if "chdir" in code:
            code = ''
        exec(code)
    else:
        help(shell)
    
