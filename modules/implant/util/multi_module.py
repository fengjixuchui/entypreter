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

import core.implant
import time
import string

class MultiModuleImplant(core.implant.Implant):

    NAME = "Multi Module Execution"
    DESCRIPTION = "Run multiple modules in succession."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/util/multi_module"

    def load(self):
        self.options.register("MODULES", "", "Modules to run in succession.", required = True)
        self.options.register("DELAY", "0", "Number of seconds between each job.", required = True)

    def run(self):
        for module in self.options.get("MODULES").split(","):
            plugin = self.shell.plugins[module.strip()]
            old_zombie = plugin.options.get("ZOMBIE")
            plugin.options.set("ZOMBIE", self.options.get("ZOMBIE"))
            plugin.run()
            plugin.options.set("ZOMBIE", old_zombie)

            delay = int(self.options.get("DELAY"))
            if delay > 0:
                time.sleep(delay)

