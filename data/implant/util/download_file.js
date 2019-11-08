try
{
    proton.http.upload("~RFILEF~", "data", ~CERTUTIL~);
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
