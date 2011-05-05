"""
MyPyGame - Events.py

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

import pygame 

class PyGameEventHandler:
    """ PyGameEventHandler
    represents one mapping between a pygame event type and
    a method to call
    """

    event_type = None
    method = None
    payload = None

    def __init__(self, event_type, method):
        """ Constructor
        """

        self.event_type = event_type
        self.method = method

    def set_payload(self, method_name):
        """ Set the payload for this handler
        """

        self.payload = method_name

class PyGameDispatcher:
    """ PyGameDispatcher

    """

    event_handlers = []

    def __init__(self):
        """ Constructor
        """

        pass

    def add(self, event_handler):
        """ Add an event handler
        """

        self.event_handlers.append(event_handler)

    def get_event_types(self):
        """ Get a list of event types that this handler
        currently has
        """

        result = []
        for event_handler in self.event_handlers:
            result.append(event_handler.event_type)
        return result

    def lookup(self, event_type):
        """ Lookup 
        """
        for event_handler in self.event_handlers:
            if event_handler.event_type in self.get_event_types():
                return True
        return False

    def get_handler(self, event_type):
        """ get_handler_name
        """

        handler = None

        for event_handler in self.event_handlers:
            if event_handler.event_type == event_type:
                handler = event_handler

        return handler

    def get_handler_name(self, event_type):
        """ get_handler_name
        """

        handler_name = None

        for event_handler in self.event_handlers:
            if event_handler.event_type == event_type:
                handler_name = event_handler.method

        return handler_name

    def get_payload(self, event_type):
        """ Get the payload associated an event handler
        """

        for event_handler in self.event_handlers:
            if event_handler.event_type == event_type:
                return event_handler.payload
        return None

    def set_payload(self, event_type, method_name):
        """ Set the payload associated an event handler within
        this dispatcher
        """

        for event_handler in self.event_handlers:
            if event_handler.event_type == getattr(pygame, event_type):
                event_handler.set_payload(method_name)

