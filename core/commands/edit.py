DESCRIPTION = "Edit the current module."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "edit %s" to edit the current module\'s python file.' % (shell.colors.colorize("py/python", shell.colors.BOLD)))
    shell.print_plain('Use "edit %s" to edit the current module\'s associated javascript file (if applicable).' % (shell.colors.colorize("js/javascript", shell.colors.BOLD)))
    shell.print_plain('Use "edit %s" to edit the current module\'s associated vbscript file (if applicable).' % (shell.colors.colorize("vbs/vbscript", shell.colors.BOLD)))
    shell.print_plain("")

def execute(shell, cmd):
    import subprocess, os

    try:
        if not os.environ['EDITOR']:
            editor = 'vi'
        else:
            editor = os.environ['EDITOR']
    except KeyError:
        editor = 'vi'

    py_file = "modules/"+shell.state+".py"
    js_file = "data/"+shell.state+".js"
    vbs_file = "data/"+shell.state+".vbs"
    dropper_file = "data/"+shell.state+".dropper"

    splitted = cmd.split()

    if len(splitted) > 1:
        ftype = splitted[1].lower()
        if ftype == "py" or ftype == "python":
            file = py_file
        elif ftype == "js" or ftype == "javascript":
            file = js_file
        elif ftype == "vbs" or ftype == "vbscript":
            file = vbs_file
        elif ftype == "dropper":
            file = dropper_file
        else:
            return

        if os.path.isfile(file):
            editcmd = [editor, file]
        else:
            return
    else:
        editcmd = [editor, py_file]
    
    subprocess.call(editcmd)
    shell.run_command('load')
