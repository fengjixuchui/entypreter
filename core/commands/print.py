import time

DESCRIPTION = "Print some text."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "print %s" to print the specified text.' % (shell.colors.colorize("TEXT", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    splitted = cmd.split()
    
    if len(splitted) > 1:
        string = " ".join(cmd.split(" ")[1:])
        if '+' in string or '-' in string or '*' in string or '/' in string or '%' in string:
            print(eval(string))
        else:
            print(string)
    else:
        help(shell)
