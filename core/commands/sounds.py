DESCRIPTION = "Turn sounds on/off."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "sounds on" to turn sounds on.')
    shell.print_plain('Use "sounds off" to turn sounds off.')
    shell.print_plain("")

def execute(shell, cmd):
    try:
        import playsound
    except:
        shell.print_error('You do not have the playsound module installed. Please run \'pip3 install playsound\' to enable this feature!')
        return

    splitted = cmd.split()

    if len(splitted) > 1:
        sw = splitted[1].lower()
        if sw == "1" or sw == "true" or sw == "on":
            from core.sounds import sounds
            shell.sounds = sounds
            shell.play_sound('ON')
            shell.print_status("Sounds: %s" % ("on" if shell.sounds else "off"))
        if sw == "0" or sw == "false" or sw == "off":
            shell.sounds = {}
            shell.print_status("Sounds: %s" % ("on" if shell.sounds else "off"))
    else:
        help(shell)
