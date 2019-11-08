try
{
    var html = new ActiveXObject("htmlfile");
    var text = html.parentWindow.clipboardData.getData("text");
    proton.work.report(text);
}
catch (e)
{
    proton.work.error(e)
}

proton.exit();
