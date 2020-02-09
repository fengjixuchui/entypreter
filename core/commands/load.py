#!/usr/bin/env python3

#            ---------------------------------------------------
#                             Proton Framework              
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import importlib
import core.plugin
import copy

DESCRIPTION = "Reload all Proton Framework modules."

def autocomplete(shell, line, text, state):
    return None

def help(shell):
    pass

def execute(shell, cmd):
    count = 0
    for key in shell.plugins:
        _key = key

        try:
            key = key.split("/")[-1]
            module = sys.modules[key]
            source = open("modules/"+_key+".py").read()
            exec(source,module.__dict__)

            for thing in dir(module):
                try:
                    thing = getattr(module, thing)

                    if issubclass(thing, core.plugin.Plugin):
                        new_thing = thing(shell)
                        new_thing.options = copy.deepcopy(shell.plugins[_key].options)
                        shell.plugins[_key] = new_thing
                        count += 1
                except TypeError as e:
                    pass
        except:
            shell.print_error("Failed to load %s!" % _key)
            pass

    shell.play_sound('LOAD')
    shell.print_good("Successfully loaded %d modules." % count)
