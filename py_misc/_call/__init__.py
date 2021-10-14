
##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Cyclic Reference
from ..misc import Misc

# Import Call Classes
from ._callable import Callable
from ._caller import Caller
from ._resolvable import Resolvable
from ._safe import Safe
from ._try import Try

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Check If Object Is a Caller
def iscaller(obj: object):
    return (hasattr(obj, '__callable__') and
        callable(obj.__callable__))

# Check If Object Is a True Caller
def istruecaller(obj: object):
    return (callable(obj) and iscaller(obj))

# Get Callable of Object
def getcallable(obj: object, bypass: bool = False):
    caller = [obj]
    while (iscaller(caller[-1]) and ((caller[-1].__pass__
        if hasattr(caller[-1], '__pass__') else False) or bypass)):
        caller.append(caller[-1].__callable__)
    return caller[-1]

# Check If Object Is a Resolvable
def isresolvable(obj: object):
    return (iscaller(obj) and
        all(hasattr(obj, attr) for attr in
        ['__resolve__', 'value', 'resolved',
        '__reject__', 'error', 'rejected',
        '__reset__', 'resolution']))

# Check If Object Is a Waitable
def iswaitable(obj: object):
    return (isresolvable(obj) and
        all(hasattr(obj, attr) for attr in
        ['wait', 'then', 'catch',
        '__thread__', '__trigger__']))

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################
