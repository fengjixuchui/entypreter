DESCRIPTION = "Display info about jobs."

def autocomplete(shell, line, text, state):
    pass

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "jobs %s" to view job results (if any).' % (shell.colors.colorize("JOB_ID", shell.colors.BOLD)))
    shell.print_plain("")

def print_job(shell, id):
    for jkey, job in shell.jobs.items():
        if job.id == int(id) and job.status_string() in ["Completed", "Failed"]:
            job.display()

def print_all_jobs(shell):
    if shell.jobs == {}:
        shell.print_error("No active jobs yet!")
        return
    
    formats = "\t{0:<5}{1:<10}{2:<20}{3:<40}"

    shell.print_plain("")

    shell.print_plain(formats.format("ID", "STATUS", "ZOMBIE", "NAME"))
    shell.print_plain(formats.format("-"*2,  "-"*6, "-"*6, "-"*4))
    for jkey, job in shell.jobs.items():
        if job.session_id != -1:
            zombie = "%s (%d)" % (job.ip, job.session_id)
        else:
            zombie = "%s (%d)" % (job.ip, -1)

        shell.print_plain(formats.format(job.id, job.status_string(), zombie, job.name))
        
    shell.print_plain("")

def execute(shell, cmd):

    splitted = cmd.split()

    if len(splitted) > 1:
        try:
            id = splitted[1]
            print_job(shell, id)
            return
        except ValueError:
            shell.print_error("Expected valid job ID!")
            return
        
    print_all_jobs(shell)
