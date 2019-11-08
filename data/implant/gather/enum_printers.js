try
{
    var WshNetwork = WScript.CreateObject("WScript.Network");
    var oPrinters = WshNetwork.EnumPrinterConnections();

    var ret = "";
    for (i = 0; i < oPrinters.length; i += 2)
    {
        ret += oPrinters.Item(i) + " = " + oPrinters.Item(i + 1) + "\n";
    }

    proton.work.report(ret);
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();