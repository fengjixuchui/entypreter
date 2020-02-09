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

import os
import sys
import core.stager
from core.payload import Payload
import random

"""
class VBScriptStager(core.stager.Stager):

    NAME = "VBScript Stager"
    DESCRIPTION = "Listens for new sessions, using VBScript for payloads."
    AUTHORS = ['Entynetproject']

    # the type of job payloads
    WORKLOAD = "vbs"

    def run(self):
        payloads = []
        payloads.append(Payload("In Memory (Windows 2000 SP3+)", self.load_file("data/stager/vbscript/mshta.cmd")))
        payloads.append(Payload("On Disk (All Windows)", self.load_file("data/stager/vbscript/disk.cmd")))

        self.start_server(payloads)

    def stage(self, server, handler, session, options):
        script = self.load_script("data/stager/vbscript/work.vbs", options, True, False)
        handler.reply(200, script)

    def job(self, server, handler, session, job, options):
        script = self.load_script("data/stager/vbscript/job.vbs", options)
        handler.reply(200, script)
"""
