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
    var path = "System\\CurrentControlSet\\Control\\Terminal Server";
    var key = "fDenyTsConnections";

    proton.registry.write(proton.registry.HKLM, path, key, ~MODE~, proton.registry.DWORD);
    var out = proton.registry.read(proton.registry.HKLM, path, key, proton.registry.DWORD);

    if (out.uValue != ~MODE~)
        throw new Error("Unable to write to registry key.");

    proton.work.report("");
}
catch(e)
{
    proton.work.error(e);
}

proton.exit()
