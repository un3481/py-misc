
##########################################################################################################################

# Modules
from .promise import Promise
from ..call import Caller

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
            __caller__ = Caller(obj.__callable__)
            __caller__.__pass__ = True
            __caller__.setargs(*obj.iargs, **obj.ikwargs)
            return Promise(__caller__)

##########################################################################################################################
