
##########################################################################################################################

# Import
import threading

# Modules
from .. import call

##########################################################################################################################
#                                                           ASYNC                                                        #
##########################################################################################################################

# Async Class
class Async(call.Caller):

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
            __caller__ = call.Caller(obj.__callable__)
            __caller__.__pass__ = True
            __caller__.setargs(*obj.iargs, **obj.ikwargs)
            return self.threading.Promise(__caller__)

    @property
    def threading(self):
        return threading
            
##########################################################################################################################
