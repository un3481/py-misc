
##########################################################################################################################

# Imports
import inspect

# Modules
from .safe import Safe
from .resolvable import Resolvable
from .methods import getcallable

##########################################################################################################################

# Safe Class
class Caller(Resolvable):

    # Init Safe
    def __init__(self, function, log=True):
        # Check Parameters
        if (not callable(function) or
            not isinstance(log, bool)):
            self = False
            return None
        # Init Resolvable
        function = Safe(function, log)
        super().__init__(function, log)
        # Set Default Caller
        self.call(lambda obj: obj.__callable__(*obj.args, **obj.kwargs))
        # Set Bypass to False
        self.__pass__ = False
        # Set Arguments
        self.args = list()
        self.iargs = list()
        self.kwargs = dict()
        self.ikwargs = dict()

    # Set Caller Arguments
    def setargs(self, *args, **kwargs):
        _params = (list(), dict())
        _call = getcallable(self.__callable__)
        params = inspect.getargspec(_call)[0]
        # Set Keyword Arguments
        for key in kwargs:
            if key in params:
                _params[1][key] = kwargs[key]
                params.remove(key)
        # Set Var Arguments
        for arg in args:
            if args.index(arg) < len(params):
                _params[0].append(arg)
        # Set Arguments
        self.args = _params[0]
        self.kwargs = _params[1]
        return _params

    # Set Caller Function
    def call(self, function):
        if not callable(function): return False
        params = inspect.getargspec(function)[0]
        if not len(params) == 1: return False
        function = Safe(function, self.__logging__)
        self.__caller__ = function
        return function

    # Call Method
    def __call__(self, *args, **kwargs):
        # Set Input Arguments
        self.iargs = args
        self.ikwargs = kwargs
        # Execute Caller
        return self.__caller__(self)

##########################################################################################################################
