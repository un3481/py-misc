
##########################################################################################################################
#                                                            CYCLE                                                       #
##########################################################################################################################

# Import Resolvable
from . import daemon

##########################################################################################################################
#                                                            CYCLE                                                       #
##########################################################################################################################

# Cycle Thread Class
class Cycle(daemon.Daemon):

    # Init Now
    def __init__(self, function, delay=None, start=True):
        # Check Parameters
        if (not callable(function) or
            not isinstance(start, bool)):
            self = False
            return None
        # Set Cyclic Try
        self.__try__ = self.misc.call.Repeat(function=function)
        self.__try__.times(None).delay(delay).timeout(None)
        self.__try__.condition(lambda obj: False)
        # Set Thread Object
        super().__init__(self.__try__, start=start, log=False)
        
##########################################################################################################################
#                                                            CYCLE                                                       #
##########################################################################################################################
