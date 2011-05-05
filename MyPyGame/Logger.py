"""
MyPyGame - Logger.py

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 


LICENSING

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version

This program is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>. 

"""

import time

class MyPyGameLogger:
    """ MyPyGameLogger

    Handle logging for MyPyGame (a wrapper for pygame)

    """
    logging_level = None
    console = 1

    def __init__(self, logging_level):
        """ Constructor
        """

        self.logging_level = logging_level

    def write(self, msg, requested_level):
        """ Write out a log entry
        """
        output = ""

        if requested_level <= self.logging_level:
            output =  "(" + str(time.time()) + ")" + msg 

            if self.console:
                print(output)
