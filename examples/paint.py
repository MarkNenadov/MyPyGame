from MyPyGame.Wrapper import PyGameWrapper
from MyPyGame.constants import *

pgw = PyGameWrapper(320, 240, 'white', LOGGING_LIGHT)
pgw.dispatcher.set_payload("MOUSEMOTION", 'sketcher')
pgw.loop()
