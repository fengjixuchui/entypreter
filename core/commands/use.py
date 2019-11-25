DESCRIPTION = "Switch to a different module."

def autocomplete(shell, line, text, state):
    import readline
    everything = readline.get_line_buffer()
    cursor_idx = readline.get_begidx()
    idx = 0
    for chunk in everything.split(" "):
        fulltext = chunk
        idx += len(chunk) + 1
        if idx > cursor_idx:
            break
    prefix, suffix = fulltext.rsplit("/",maxsplit=1) if "/" in fulltext else ("",fulltext)
    if prefix:
        prefix += "/"

    options = []
    tmp = list(shell.plugins.keys())
    for plugin in shell.plugins:
        tmp.append(plugin.split("/")[-1])
    for plugin in tmp:
        if not plugin.startswith(fulltext):
            continue
        chunk = plugin[len(prefix):]
        if "/" in chunk:
            options.append(chunk.split("/")[0]+"/")
        else:
            options.append(chunk+" ")
    options = list(sorted(set(options)))
    try:
        return options[state]
    except:
        return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "use %s" to switch to the specified module.' % (shell.colors.colorize("MODULE", shell.colors.BOLD)))
    shell.print_plain("")

def modules(shell, module):
    for i in shell.plugins:
        if module == i.split('/')[-1]:
            return 0
    return 1
    
def execute(shell, cmd):
    splitted = cmd.split()

    if len(splitted) > 1:
        module = splitted[1]
        if modules(shell, module):
            shell.print_error("No module named %s." % (module))
            return
        if "/" not in module:
            module = [k for k in shell.plugins if k.lower().split('/')[-1] == module.lower()][0]
        shell.previous = shell.state
        shell.state = module
        
    else:
        help(shell)
