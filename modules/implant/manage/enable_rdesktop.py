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

class EnableRDesktopJob(core.job.Job):
    def create(self):
        mode = "0" if self.options.get("ENABLE") == "true" else "1"
        self.options.set("MODE", mode)
    def done(self):
        self.results = "Completed!"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain(str(self.errno))

class EnableRDesktopImplant(core.implant.Implant):

    NAME = "Enable Remote Desktop"
    DESCRIPTION = "Enables RDP on the target system."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/manage/enable_rdesktop"

    def load(self):
        self.options.register("ENABLE", "true", "Toggle to enable or disable.", enum=["true", "false"])
        self.options.register("MODE", "", "The value for this script.", hidden=True)

    def job(self):
        return EnableRDesktopJob

    def run(self):
        workloads = {}
        #workloads["vbs"] = self.load_script("data/implant/manage/enable_rdesktop.vbs", self.options)
        workloads["js"] = "data/implant/manage/enable_rdesktop.js"

        self.dispatch(workloads, self.job)
