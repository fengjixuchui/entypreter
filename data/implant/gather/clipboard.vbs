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

Set objHTML = CreateObject("htmlfile")
text = objHTML.ParentWindow.ClipboardData.GetData("text")

KoReportWork text

KoExit

'Set ie = CreateObject("InternetExplorer.Application")
'ie.Visible = 0
'ie.Navigate2 "C:\Users\David Candy\Desktop\Filter.html"
'Do
''  wscript.sleep 100
'Loop until ie.document.readystate = "complete"
'txt=ie.document.parentwindow.clipboardData.GetData("TEXT")
'ie.quit
'If IsNull(txt) = true then
'outp.writeline "No text on clipboard"
'else
'outp.writeline txt
'End If
