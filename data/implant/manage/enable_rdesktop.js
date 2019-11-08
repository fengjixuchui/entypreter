try
{
    var path = "System\\CurrentControlSet\\Control\\Terminal Server";
    var key = "fDenyTsConnections";

    proton.registry.write(proton.registry.HKLM, path, key, ~MODE~, proton.registry.DWORD);
    var out = proton.registry.read(proton.registry.HKLM, path, key, proton.registry.DWORD);

    if (out.uValue != ~MODE~)
        throw new Error("Unable to write to registry key.");

    proton.work.report("");
}
catch(e)
{
    proton.work.error(e);
}

proton.exit()
