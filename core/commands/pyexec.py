DESCRIPTION = "Eval some python code."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain("Usage: pyexec <code>")
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()
    
    if len(splitted) > 1:
        code = " ".join(cmd.split(" ")[1:])
        exec(code)
    else:
        help(shell)
    
