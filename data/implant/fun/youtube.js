try
{
    var ie = new ActiveXObject("InternetExplorer.Application");
    ie.Visible = 0;
    ie.Navigate2("~VIDEOURL~");

    for (var i = 0; i < 50; ++i)
    {
        proton.WS.SendKeys(String.fromCharCode(0xAF));
    }

    proton.shell.run("ping 127.0.0.1 -n ~SECONDS~", false);
    ie.Quit();
}
catch (e)
{
    proton.work.error(e);
}
proton.exit();
