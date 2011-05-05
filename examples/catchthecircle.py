from MyPyGame.Wrapper import PyGameWrapper
from PyGame.Logging import ConsoleLoggingAdapter
from MyPyGame.constants import *

#
# Instead of using ConsoleLoggingAdapter, you could
# use one of the following:
#
#from MyPyGame.Logging import TextFileLoggingAdapter

pgw = PyGameWrapper(320, 240, 'white', ConsoleLoggingAdapter(), LOGGING_LIGHT)
pgw.dispatcher.set_payload("MOUSEMOTION", 'sketcher')
pgw.loop()
