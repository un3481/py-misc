
##########################################################################################################################

from .methods import locale

##########################################################################################################################

# Callable Class
class Callable:

    # Init Callable
    def __init__(self, function):
        # Check Parameters
        if not callable(function):
            self = False
            return None
        # Nest Objects
        self.__callable__ = function

    @property
    def __proxy__(self):
        return self.__callable__

    @property
    def __locale__(self):
        return locale(self)

##########################################################################################################################
