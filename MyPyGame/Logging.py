"""
MyPyGame - Logging.py

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

class LogDataAdapter(object):
    """ LogAdapter

    Provides interface between specific data storage and 
    MyPyGameLogger, its children get passed to MyPyGameLogger
    constructor

    """

    def __init__(self):
        pass


    def save2log(self, data):
        timestamp = time.time()
        self.write("(" + str(timestamp) + ")" + data)

class TextFileLoggingAdapter(LogDataAdapter):
    """ TextFileLoggingAdapter

    Allow logging to a text file. Can be passed to MyPyGameLogger's
    constructor

    """

    f = None

    def __init__(self, file_name):
        super(TextFileLoggingAdapter, self).__init__()
        
        self.f = open(file_name, 'a')

    def save2log(self, data):
        """ save log data into a textfile
        """

        super(TextFileLoggingAdapter, self).save2log(data)

    def write(self, data):
        self.f.write(data + "\n")

    def close(self):
        self.f.close()
        super(TextFileLoggingAdapter, self).close()

class ConsoleLoggingAdapter(LogDataAdapter):
    """ ConsoleLoggingAdapter

    Allow logging to a console. Can be passed to MyPyGameLogger's
    constructor

    """

    f = None

    def __init__(self):
        super(ConsoleLoggingAdapter, self).__init__()
        

    def save2log(self, data):
        """ print data into the console
        """

        super(ConsoleLoggingAdapter, self).save2log(data)

    def write(self, data):
        print(data)

    def close(self):
        super(ConsoleLoggingAdapter, self).close()

class DBILoggingAdapter(LogDataAdapter):
    """ DBILoggingAdapter

    Allow logging to any databse that supports the DBI 2.0
    library. Can be passed to MyPyGameLogger's constructor

    Note: MyPyGame assumes that the following table exists (although 
    you can adjust the table name utilized by passing it as a second 
    parameter to DBILoggingAdapter, namely the table name as a string):


        CREATE  TABLE logs ("entry" VARCHAR NOT NULL )

    """

    conn = None
    cursor = None
    table_name = None

    def __init__(self, conn, table_name='logs'):

        super(DBILoggingAdapter, self).__init__()
        
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def save2log(self, data):
        """ save log data into a textfile
        """

        super(DBILoggingAdapter, self).save2log(data)

    def write(self, data):
        self.cursor.execute("INSERT INTO " + self.table_name + " VALUES('"+data+"')")
        self.conn.commit()

    def close(self):
        self.cursor.close
        super(DBILoggingAdapter, self).close()


class MyPyGameLogger:
    """ MyPyGameLogger

    Handle logging for MyPyGame (a wrapper for pygame)

    """
    logging_level = None
    log_adapter = None

    def __init__(self, logging_level, log_adapter):
        """ Constructor
        """

        self.logging_level = logging_level
        self.log_adapter = log_adapter

    def write(self, msg, requested_level):
        """ Write out a log entry
        """
        output = ""

        if requested_level <= self.logging_level:
            if not self.log_adapter.write(msg):
                return False
            return True
        return False
