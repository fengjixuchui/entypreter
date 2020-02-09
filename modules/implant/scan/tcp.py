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

class ScanTCPJob(core.job.Job):
    def create(self):
        hosts = self.parse_ips(self.options.get("RHOSTS"))
        ports = self.parse_ports(self.options.get("RPORTS"))

        self.options.set("RHOSTSARRAY", self.make_js_array("ips", hosts))
        self.options.set("RPORTSARRAY", self.make_js_array("ports", ports))
    def done(self):
        self.display()

    def print_port(self, lines):
        status = lines[0]
        ip = lines[1]
        port = lines[2]
        if lines[3] != "0":
            errno = (int(lines[3]) + 2**32)
        errno = "%08x" % (int(lines[3]) + 2**32 if lines[3] != "0" else 0x0)

        formats = 'Zombie %d: Job %d (%s) {0:<20}{1:<10}{2:<20}{3:<10}' % (self.session.id, self.id, self.name)

        #color = []
        color = [self.shell.colors.RED]

        if status == "open":
            color = [self.shell.colors.GREEN]
            printer = self.shell.print_good
        elif status == "closed":
            printer = self.shell.print_status
        elif status == "unsupported":
            printer = self.shell.print_warning
        else:
            printer = self.shell.print_error

        status = self.shell.colors.colorize(status, color)
        #port = self.shell.colors.colorize(port, color)
        msg = formats.format(ip, port, status, errno)
        self.results += msg + "\n"
        printer(msg)


    def report(self, handler, data):
        if data != b"done":
            lines = data.decode().split("\n")
            self.print_port(lines)
            handler.reply(200)
            return

        super(ScanTCPJob, self).report(handler, data)

    def display(self):
        pass
        #self.shell.print_plain("PID Start Code: %s" % self.data)

class ScanTCPImplant(core.implant.Implant):

    NAME = "Scan TCP"
    DESCRIPTION = "Looks for open TCP ports."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/scan/tcp"

    def load(self):
        self.options.register("RHOSTS", "", "Name/IP of the remotes.")
        self.options.register("RHOSTSARRAY", "", "Script array.", hidden=True)
        self.options.register("RPORTS", "22,80,135,139,443,445,3389", "Ports to scan.")
        self.options.register("RPORTSARRAY", "", "Script array.", hidden=True)
        self.options.register("TIMEOUT", "3", "Longer is more accurate.")
        self.options.register("CHECKLIVE", "true", "Check if host is up before checking ports.", enum=["true", "false"])

    def job(self):
        return ScanTCPJob

    def run(self):
        payloads = {}
        #payloads["vbs"] = self.load_script("data/implant/scan/tcp.vbs", options)
        payloads["js"] = "data/implant/scan/tcp.js"
        #print(payloads["js"])


        self.dispatch(payloads, self.job)
