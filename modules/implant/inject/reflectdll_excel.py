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

class ExcelReflectJob(core.job.Job):
    def done(self):
        self.results = "Completed"
        self.display()

    def display(self):
        pass
        #self.shell.print_plain(str(self.errno))

class ExcelReflectImplant(core.implant.Implant):

    NAME = "Reflective DLL via Excel"
    DESCRIPTION = "Executes an arbitrary reflective DLL."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/inject/reflectdll_excel"

    def load(self):
        self.options.register("DLLPATH", "", "The DLL to inject.", required=True)

    def job(self):
        return ExcelReflectJob

    def run(self):
        workloads = {}
        #workloads["vbs"] = self.load_script("data/implant/manage/enable_rdesktop.vbs", self.options)
        workloads["js"] = "data/implant/inject/reflectdll_excel.js"

        self.dispatch(workloads, self.job)
