DESCRIPTION = "Display info about a job."

def autocomplete(shell, line, text, state):
    pass

def help(shell):
    shell.print_plain("")
    shell.print_plain("Use %s to view job results (if any)." % (shell.colors.colorize("jobs JOB_ID", shell.colors.BOLD)))
    shell.print_plain("")

def print_job(shell, id):
    for job in shell.jobs:
        if job.id == int(id) and job.status_string() in ["Complete", "Failed"]:
            job.display()

def print_all_jobs(shell):
    formats = "\t{0:<5}{1:<10}{2:<20}{3:<40}"

    shell.print_plain("")

    shell.print_plain(formats.format("ID", "STATUS", "session", "NAME"))
    shell.print_plain(formats.format("-"*4,  "-"*9, "-"*10, "-"*20))
    for job in shell.jobs:
        if job.session_id != -1:
            session = "%s (%d)" % (job.ip, job.session_id)
        else:
            session = "%s (%d)" % (job.ip, -1)

        shell.print_plain(formats.format(job.id, job.status_string(), session, job.name))


    shell.print_plain("")



def execute(shell, cmd):

    splitted = cmd.split()

    if len(splitted) > 1:
        id = splitted[1]
        print_job(shell, id)
        return

    print_all_jobs(shell)
