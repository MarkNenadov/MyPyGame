from MyPyGame.Wrapper import PyGameWrapper
from MyPyGame.Logging import ConsoleLoggingAdapter
#
# Instead of using ConsoleLoggingAdapter, you could
# use one of the following:
#
#from MyPyGame.Logging import TextFileLoggingAdapter
#from MyPyGame.Logging import DBILoggingAdapter
from MyPyGame.constants import *

pgw = PyGameWrapper(320, 240, 'white', ConsoleLoggingAdapter(), LOGGING_LIGHT)
pgw.dispatcher.set_payload("MOUSEMOTION", 'sketcher')
pgw.loop()
