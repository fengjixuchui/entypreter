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

class VoiceJob(core.job.Job):
    def done(self):
        self.display()

    def display(self):
        self.results = "Completed!"
        #self.shell.print_plain(self.data)

class VoiceImplant(core.implant.Implant):

    NAME = "Voice"
    DESCRIPTION = "Makes the computer speak a message."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/fun/voice"

    def load(self):
        self.options.register("MESSAGE", "I can't do that Dave", "Message to speak.")

    def job(self):
        return VoiceJob

    def run(self):
        payloads = {}
        #payloads["vbs"] = self.load_script("data/implant/fun/voice.vbs", self.options)
        payloads["js"] = "data/implant/fun/voice.js"

        self.dispatch(payloads, self.job)
