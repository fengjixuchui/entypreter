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
    var computer = ".";
    var wmi = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\" + computer + "\\root\\cimv2");

    // https://msdn.microsoft.com/en-us/library/aa394189(v=vs.85).aspx
    var sessions = wmi.ExecQuery("Select * from Win32_LogonSession Where LogonType = 2 OR LogonType = 10");

    if (sessions.Count == 0)
    {
        proton.work.report("No interactive users found.")
    }
    else
    {
        for (var e = new Enumerator(sessions); !e.atEnd(); e.moveNext())
        {
            var session = e.item();

            var query = "";
            query += "Associators of {Win32_LogonSession.LogonId=" + session.LogonId;
            query += "} Where AssocClass=Win32_LoggedOnUser Role=Dependent";
            var users = wmi.ExecQuery(query);

            for (var f = new Enumerator(users); !f.atEnd(); f.moveNext())
            {
                var user = f.item();
                var info = user.Caption;
                proton.work.report(info);
            }
        }
    }
} catch (e)
{
    proton.work.error(e);
}
proton.work.report("Complete");
proton.exit();
