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

import core.extant
import core.repeatjobclock
import core.restoreclock

''' Kick off clocks '''
class Tick(object):

    def __init__(self, shell):
        self.start_timers(shell)

    def start_timers(self, shell):
        self.extant = core.extant.Extant(shell)
        self.repeatjobclock = core.repeatjobclock.RepeatJobClock(shell)
        self.restoreclock = core.restoreclock.RestoreClock(shell)
