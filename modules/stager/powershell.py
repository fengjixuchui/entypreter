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
import random

"""
class PowerShellStager(core.stager.Stager):

    NAME = "PowerShell Stager"
    DESCRIPTION = "Listens for new sessions, using PowerShell for payloads."
    AUTHORS = ['Entynetproject']

    def run(self):
        payloads = {}
        payloads["In Memory"] = self.load_file("data/stager/powershell/memory.cmd")

        self.start_server(payloads)

    def stage(self, server, handler, session):
        script = self.load_script("data/stager/powershell/payload.ps1")
        handler.send_ok(script)
"""
