DESCRIPTION = "Unset a variable for the current module."

def autocomplete(shell, line, text, state):

    # todo, here we can provide some defaults for bools/enums? i.e. True/False
    if len(line.split()) > 2:
        return None

    env = shell.plugins[shell.state]
    options = [x.name + " " for x in env.options.options if x.name.upper().startswith(text.upper()) and not x.hidden]
    options += [x.alias + " " for x in env.options.options if x.alias.upper().startswith(text.upper()) and not x.hidden and x.alias]

    try:
        return options[state]
    except:
        return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "unset %s" to unset the value for the specified option.' % (shell.colors.colorize("OPTION", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    env = shell.plugins[shell.state]

    splitted = cmd.split()
    if len(splitted) > 1:
        key = splitted[1].upper()

        value = env.options.get(key)
        if value != None:

            value = ""
            if not env.options.set(key, value):
                shell.print_error("That option is invalid!")
                return

            shell.print_good("%s => %s" % (key, value))
        else:
            shell.print_error("Option '%s' not found." % (key))
            
    else:
        help(shell)
