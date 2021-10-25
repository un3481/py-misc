
##########################################################################################################################

# Imports
import time
import datetime

# Modules
from .. import time as _time
from . import safe
from . import resolvable

##########################################################################################################################
#                                                            TRY                                                         #
##########################################################################################################################

# Try Class
class Repeat(resolvable.Resolvable):

    # Init Daemon
    def __init__(self, times=3, delay=1, timeout=60, function=None, condition=None):
        # Check Parameters
        if ((not isinstance(times, int) and times != None) or
            (not isinstance(delay, int) and
            not isinstance(delay, float) and delay != None) or
            (not isinstance(timeout, int) and
            not isinstance(timeout, float) and timeout != None) or
            (function != None and not callable(function)) or
            (condition != None and not callable(condition))):
            self = False
            return None
        # Fix None Functions
        if function == None: function = (lambda: None)
        if condition == None: condition = (lambda obj: obj.resolved)
        # Init Resolvable
        function = safe.Safe(function, False)
        super().__init__(function, False)
        # Set Bypass to False
        self.__pass__ = False
        # Set Attempts Object
        self.__attempts__ = list()
        # Set Parameters
        self.__times__ = int(3)
        self.__delay__ = float(0)
        self.__delta__ = _time.Delta()
        self.__timeout__ = datetime.timedelta(seconds=60)
        # Call Setters
        self.times(times)
        self.delay(delay)
        self.timeout(timeout)
        self.condition(condition)

    # Times Setter
    def times(self, times):
        if (not isinstance(times, int) and
            times != None): return False
        # Set Times
        self.__times__ = times
        # Return Self
        return self

    # Delay Setter
    def delay(self, delay):
        if (not isinstance(delay, int) and
            not isinstance(delay, float) and
            delay != None): return False
        # Fix None Delay
        if delay == None: delay = 0
        self.__delay__ = float(delay)
        # Return Self
        return self

    # Timeout Setter
    def timeout(self, timeout):
        td = datetime.timedelta
        if (not isinstance(timeout, int) and
            not isinstance(timeout, float) and
            not isinstance(timeout, td) and
            timeout != None): return False
        # Set Timeout
        if not isinstance(timeout, td) and timeout != None:
            timeout = datetime.timedelta(seconds=timeout)
        self.__timeout__ = timeout
        # Return Self
        return self

    # Set Callable
    def call(self, function):
        # Check Parameters
        if (not callable(function) and
            function != None): return False
        # Fix None Function
        function = (function if function != None
            else (lambda: None))
        function = safe.Safe(function)
        self.__callable__ = function
        return function

    # Set Condition
    def condition(self, function):
        # Check Parameters
        if (not callable(function) and
            function != None): return False
        # Fix None Function
        function = (function if function != None
            else (lambda obj: obj.resolved))
        function = safe.Safe(function)
        self.__condition__ = function
        return function

    # Caller to Try
    def __call__(self, *args, **kwargs):
        # Reset Delta
        self.__delta__.reset()
        # Try Loop
        while ((self.__times__ == None or
            len(self.__attempts__) < self.__times__) and
            (self.__timeout__ == None or
            self.__delta__.since.init < self.__timeout__) and
            not self.done):
            # Execute Callable
            value = self.__callable__(*args, **kwargs)
            # Fix Delta
            if self.__timeout__ == None: self.__delta__.reset()
            # Fix List Length
            if self.__times__ == None: self.__attempts__ = list()
            # Append Attempt
            self.__attempts__.append(dict(
                resolved = self.__callable__.resolved,
                rejected = self.__callable__.rejected,
                value = self.__callable__.value,
                error = self.__callable__.error))
            # Compute Condition
            condition = self.__condition__(self.__callable__)
            if condition: self.__resolve__(value)
            # Wait Delay
            time.sleep(self.__delay__)
        # Reject
        if not self.resolved:
            self.__reject__('Max Attempts Exeeded')
        # Return Resolution
        return self.resolution
    
##########################################################################################################################
