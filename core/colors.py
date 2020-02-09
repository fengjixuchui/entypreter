#!/usr/bin/env python3

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

class Colors(object):
    def __init__(self):
        self.ENDC = '\033[0m'

        self.RED = '31'
        self.GREEN = '32'
        self.YELLOW = '33'
        self.BLUE = '34'
        self.CYAN = '36'

        self.NORMAL = '0'
        self.BOLD = '1'
        self.WHITE = '77'
        self.UNDERLINE = '2'

    def error(self, text):
        return self.colorize(text, [self.RED, self.BOLD])

    def warning(self, text):
        return self.colorize(text, [self.YELLOW, self.BOLD])

    def good(self, text):
        return self.colorize(text, [self.GREEN, self.BOLD])

    def status(self, text):
        return self.colorize(text, [self.BLUE, self.BOLD])
    
    def other(self, text):
        return self.colorize(text, [self.WHITE, self.BOLD])

    def colorize(self, text, options, readline=False):
        start = ""
        ENDCC="\033[0m"
        if readline:
            start += "\001"
        start += '\033['
        start += ";".join(options)
        start += "m"
        if readline:
            start += "\002"
            end = "\001" + ENDCC + "\002"
        else:
            end = ENDCC

        return start + text + end
    
    def colorize_prompt(self, text, options, readline=False):
        start = ""
        ENDC = "\033[0m"
        start += "\001"
        start += '\033['
        start += ";".join(options)
        start += "m"
        start += "\002"
        end = "\001" + ENDC + "\002"

        return start + text + end
    
    def get_prompt(self, state, isreadline = True):
        import os
        glyph = "#"
        last = state.split("/")[-1]
        state = [s[0:3] for s in state.split("/")[:-1]]
        state.append(last)
        state = "/".join(state)
        return "%s%s: %s%s" % (self.colorize_prompt("(", [self.GREEN], isreadline),
                                 self.colorize_prompt("proton", [self.BOLD], isreadline),
                                 self.colorize_prompt(state, [self.CYAN], isreadline),
                                 self.colorize_prompt(")" + glyph + " ", [self.GREEN], isreadline))
