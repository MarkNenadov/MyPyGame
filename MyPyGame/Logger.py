import time

class MyPyGameLogger:
    logging_level = None
    console = 1

    def __init__(self, logging_level):
        self.logging_level = logging_level

    def write(self, msg, requested_level):
        """ Write out a log entry
        """
        output = ""

        if requested_level <= self.logging_level:
            output =  "(" + str(time.time()) + ")" + msg 

            if self.console:
                print(output)
