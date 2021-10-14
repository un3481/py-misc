
##########################################################################################################################
#                                                           ASYNC                                                        #
##########################################################################################################################

# Import Caller
from _call import Caller

##########################################################################################################################
#                                                           ASYNC                                                        #
##########################################################################################################################

# Async Class
class Async(Caller):

    # Init Async
    def __init__(self, function, log=False):
        # Check Parameters
        if (not callable(function) or
            not isinstance(log, bool)):
            self = False
            return None
        # Init Caller
        super().__init__(function, log)
        # Caller to Promise
        @self.call
        def __promise__(obj):
            __caller__ = self.misc.call.Caller(obj.__callable__)
            __caller__.__pass__ = True
            __caller__.setargs(*obj.iargs, **obj.ikwargs)
            return self.threading.promise(__caller__)

    @property
    def threading(self):
        return self.misc.threading
            
##########################################################################################################################
#                                                           ASYNC                                                        #
##########################################################################################################################
