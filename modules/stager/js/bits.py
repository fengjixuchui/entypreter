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

import core.stager
import core.loader

class BitsadminStager(core.stager.StagerWizard):

    NAME = "JScript Bitsadmin Stager"
    DESCRIPTION = "Listens for new sessions, using JScript Bitsadmin for payloads."
    AUTHORS = ['Entynetproject']

    WORKLOAD = "js"

    def __init__(self, shell):
        super(BitsadminStager, self).__init__(shell) # stupid hack inc!
        self.options.set("ENDPOINTTYPE", ".wsf")
        self.options.set("OBFUSCATE", "")

    def load(self):
        #self.options.set("SRVPORT", 9999)
        self.port = 9995

        self.stdlib = core.loader.load_script('data/stager/js/stdlib.js')
        self.stage = core.loader.load_script('data/stager/js/stage.js')
        self.stagetemplate = core.loader.load_script("data/stager/js/bitsadmin/template.wsf")
        self.stagecmd = core.loader.load_script("data/stager/js/bitsadmin/bitsadmin.cmd")
        self.forktemplate = core.loader.load_script("data/stager/js/mshta/template.hta")
        self.forkcmd = core.loader.load_script("data/stager/js/rundll32/rundll32.cmd")
        self.workload = "js"
