try
{
    var voiceObj = new ActiveXObject("sapi.spvoice");

    for (var i = 0; i < 50; ++i)
    {
        proton.WS.SendKeys(String.fromCharCode(0xAF));
    }
    voiceObj.Speak("~MESSAGE~");
    proton.work.report("");
}
catch (e)
{
    proton.work.error(e);
}
proton.exit();
