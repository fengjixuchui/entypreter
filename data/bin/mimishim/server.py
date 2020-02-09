#!/usr/bin/env python

#            ---------------------------------------------------
#                             Proton Framework              
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

from http.server import BaseHTTPRequestHandler, HTTPServer
from emu.powerkatz32 import x32
from emu.powerkatz64 import x64
import base64

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        self.wfile.write(bytes(self.requestline, "utf8"))
        return

  def do_POST(self):
      # Send response status code
      self.send_response(200)

      # Send headers
      self.send_header('Content-type','octet/stream')
      self.end_headers()


      if(self.headers['UUIDHEADA'] == 'mimidllx32'):
          self.wfile.write(base64.b64decode(x32))
      if(self.headers['UUIDHEADA'] == 'mimidllx64'):
          self.wfile.write(base64.b64decode(x64))
      if(self.headers['UUIDHEADA'] == 'mimishimx64'):
          with open("mimishimx64.dll", 'rb') as f:
              self.wfile.write(f.read())
      return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
