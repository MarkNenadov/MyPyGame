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
        self.event_type = event_type
        self.method = method

    def set_payload(self, method_name):
        self.payload = method_name

class PyGameDispatcher:
    event_handlers = []

    def __init__(self):
        pass

    def add(self, event_handler):
        self.event_handlers.append(event_handler)

    def get_event_types(self):
        result = []
        for event_handler in self.event_handlers:
            result.append(event_handler.event_type)
        return result

    def lookup(self, event_type):
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

    def get_payload(self, event_type, method_name):
        for event_handler in self.event_handlers:
            if event_handler.event_type == event_type:
                return event_handler.payload
        return None

    def set_payload(self, event_type, method_name):
        for event_handler in self.event_handlers:
            if event_handler.event_type == getattr(pygame, event_type):
                event_handler.set_payload(method_name)

