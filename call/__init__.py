
##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Cyclic Reference
from py_misc import Misc

# Import Call Classes
from .callable import Callable
from .caller import Caller
from .resolvable import Resolvable
from .safe import Safe
from '.try' import Try

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Check If Object Is a Caller
def iscaller(self, obj=self):
    return (hasattr(obj, '__callable__') and
        callable(obj.__callable__))

# Check If Object Is a True Caller
def istruecaller(self, obj=self):
    return (callable(obj) and self.iscaller(obj))

# Get Callable of Object
def getcallable(self, obj=self, bypass=False):
    caller = [obj]
    while (self.iscaller(caller[-1]) and ((caller[-1].__pass__
        if hasattr(caller[-1], '__pass__') else False) or bypass)):
        caller.append(caller[-1].__callable__)
    return caller[-1]

# Check If Object Is a Resolvable
def isresolvable(self, obj=self):
    return (self.iscaller(obj) and
        all(hasattr(obj, attr) for attr in
        ['__resolve__', 'value', 'resolved',
        '__reject__', 'error', 'rejected',
        '__reset__', 'resolution']))

# Check If Object Is a Waitable
def iswaitable(self, obj=self):
    return (self.isresolvable(obj) and
        all(hasattr(obj, attr) for attr in
        ['wait', 'then', 'catch',
        '__thread__', '__trigger__']))

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################
