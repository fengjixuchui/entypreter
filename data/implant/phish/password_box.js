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
  // cool stuff!
  // http://with-love-from-siberia.blogspot.com/2009/12/msgbox-inputbox-in-jscript.html

  // but it didn't work? :[

/*
  var vb = {};

  vb.Function = function(func)
  {
      return function()
      {
          return vb.Function.eval.call(this, func, arguments);
      };
  };


  vb.Function.eval = function(func)
  {
      var args = Array.prototype.slice.call(arguments[1]);
      for (var i = 0; i < args.length; i++) {
          if ( typeof args[i] != 'string' ) {
              continue;
          }
          args[i] = '"' + args[i].replace(/"/g, '" + Chr(34) + "') + '"';
      }

      var vbe;
      alert("yo")
      vbe = new ActiveXObject('ScriptControl');
      vbe.Language = 'VBScript';

      return vbe.eval(func + '(' + args.join(', ') + ')');
  };
*/

  /**
   * InputBox(prompt[, title][, default][, xpos][, ypos][, helpfile, context])
   */
  //var InputBox = vb.Function('InputBox');

  //  var a = InputBox("~MESSAGE~")

    var a = prompt("~MESSAGE~", "");
    proton.work.report(a);

} catch (e) {
    proton.work.error(e);
}

proton.exit();
