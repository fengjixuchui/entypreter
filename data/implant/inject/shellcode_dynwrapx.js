try
{
    proton.http.download("~DIRECTORY~/dynwrapx.dll", "~DLLUUID~");
    proton.http.download("~DIRECTORY~/dynwrapx.manifest", "~MANIFESTUUID~");

    proton.work.report("Success");
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
