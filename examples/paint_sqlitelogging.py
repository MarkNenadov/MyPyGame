""" Shows the paint program utilizing sqlite logging using MyPyGame's
DBILoggingAdapter

Note: MyPyGame assumes that the following table exists (although you can adjust
the table name utilized by passing it as a second parameter to 
DBILoggingAdapter, namely the table name as a string):

        CREATE  TABLE logs ("entry" VARCHAR NOT NULL )

So far, this has been tested with SQLite 3.

"""

import sqlite3

from MyPyGame.Wrapper import PyGameWrapper
from MyPyGame.Logging import DBILoggingAdapter

from MyPyGame.constants import *

db_conn = sqlite3.connect("C:/mypygame.sqlite")

pgw = PyGameWrapper(320, 240, 'white', DBILoggingAdapter(db_conn), LOGGING_LIGHT)
pgw.dispatcher.set_payload("MOUSEMOTION", 'sketcher')
pgw.loop()
