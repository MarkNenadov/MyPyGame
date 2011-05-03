import sys
import time

from MyPyGame.Logger import MyPyGameLogger
from MyPyGame.Events import PyGameDispatcher
from MyPyGame.Events import PyGameEventHandler
from MyPyGame.constants import *

try:
    import pygame
except ImportError:
    print( "Critical Error: Can't import requirement (pygame)")

class PyGameWrapper:
    width = 0
    height = 0
    colormap = {'black':(0,0,0), 'white':(255,255,255)}
    event_handler = {}
    dispatcher = None
    mouse_loc = None
    mouse_button_status = 0
    last_mouse_button_down = None
    logger = None

    screen = None

    def __init__(self, width, height, color_name, logging_level=LOGGING_NORMAL):
        """ constructor
        initialize pygame, set size of window, init screen,
        build event handler mapping

        """
        self.logger = MyPyGameLogger(logging_level)
        pygame.init()
        self.set_size(width, height)
        self.init_screen(color_name)

        self.dispatcher = PyGameDispatcher()
        self.dispatcher.add(PyGameEventHandler(pygame.QUIT, 'e_quit'))
        self.dispatcher.add(PyGameEventHandler(pygame.MOUSEMOTION, 'e_mouse_motion'))
        self.dispatcher.add(PyGameEventHandler(pygame.K_ESCAPE, 'e_quit'))
        self.dispatcher.add(PyGameEventHandler(pygame.K_UP, 'e_key_up'))
        self.dispatcher.add(PyGameEventHandler(pygame.K_DOWN, 'e_key_down'))
        self.dispatcher.add(PyGameEventHandler(pygame.K_LEFT, 'e_key_left'))
        self.dispatcher.add(PyGameEventHandler(pygame.K_RIGHT, 'e_key_right'))
        self.dispatcher.add(PyGameEventHandler(pygame.MOUSEBUTTONDOWN, 'e_mouse_button_down'))
        self.dispatcher.add(PyGameEventHandler(pygame.MOUSEBUTTONUP, 'e_mouse_button_up'))


    def get_size(self):
        """ get size
        Get the size of the Window
        """
        return self.width, self.height

    def get_mouse_loc(self):
        """ get_mouse_loc
        """
        return self.mouse_loc

    def get_mouse_downtime(self):
        if self.mouse_button_status:
            return time.time() - self.last_mouse_button_down
        return None


    def set_size(self, width, height):
        """ set_size
        Set the size of the window
        """

        self.width = width
        self.height = height

    def set_mouse_loc(self, location):
        """ get_mouse_loc
        """
        self.mouse_loc = location


    def init_screen(self, color_name):
        """ init_screen
        create the screen and fill it with given color
        """
        self.screen = pygame.display.set_mode(self.get_size())
        self.screen.fill(self.colormap[color_name])
        self.logger.write("Initialized screen", 1)

    def __process_event(self, event_type):
        """ process_event
        process events that occur within loop()
        """
    
        if self.dispatcher.lookup(event_type):
            event_method = self.dispatcher.get_handler_name(event_type)
            if event_method != None:
                payload = self.dispatcher.get_handler(event_type).payload
                getattr(self, event_method)(payload)


    def e_quit(self, payload=None):
        """ Quit event handler
        """
        sys.exit()

    def e_mouse_motion(self, payload=None):
        """ Mouse motion event handler
        """
        self.logger.write("User moved mouse to " + str(pygame.mouse.get_pos()), LOGGING_NORMAL)
        self.set_mouse_loc(pygame.mouse.get_pos())

        if payload != None:
            getattr(self, payload)()

    def e_key_up(self, payload=None):
        """ Up key event handler
        """
        self.logger.write("User pressed up key", LOGGING_LIGHT)

    def e_key_right(self, payload=None):
        """ Right key event handler
        """
        self.logger.write("User pressed right key", LOGGING_LIGHT)

    def e_key_left(self, payload=None):
        """ Left key event handler
        """
        self.logger.write("User pressed left key", LOGGING_LIGHT)

    def e_key_down(self, payload=None):
        self.logger.write("User pressed down key", LOGGING_LIGHT)

    def e_mouse_button_down(self, payload=None):
        self.logger.write("User pressed mouse button down", LOGGING_LIGHT)
        self.mouse_button_status = 1
        self.last_mouse_button_down = time.time()

    def e_mouse_button_up(self, payload=None):
        self.logger.write("User lifted off mouse button (it was down for " + \
                          str(self.get_mouse_downtime()) + " seconds)", LOGGING_LIGHT)
        self.mouse_button_status = 0


    def sketcher(self, size=5, color='black'):
        if self.mouse_button_status == 1:
            pygame.draw.circle(self.screen, self.colormap[color], self.get_mouse_loc(), size, 0)


    def loop(self):
        count = 0
        while 1:
            self.logger.write("Main loop iteration #" + str(count), LOGGING_CRAZY)
            for event in pygame.event.get():
                self.__process_event(event.type)
            pygame.display.flip()
            pygame.error
            count += 1

