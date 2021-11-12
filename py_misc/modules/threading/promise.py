
##########################################################################################################################

# Modules
from .. import call
from . import daemon

##########################################################################################################################
#                                                         PROMISE                                                        #
##########################################################################################################################

# Promise Class
class Promise(daemon.Daemon):
    
    # Init Promise
    def __init__(self, function, start=True):
        # Check Parameters
        if (not callable(function) or
            not isinstance(start, bool)):
            self = False
            return None
        # Set Caller
        self.__caller__ = call.Caller(function, log=False)
        self.__caller__.__pass__ = True
        # Set Caller Arguments
        self.__caller__.setargs(*self.args, **self.kwargs)
        # Set Caller Call
        @self.__caller__.call
        def __promise__(obj):
            obj.__callable__(*obj.args, **obj.kwargs)
            if self.resolved: self.__then__(self.value)
            elif self.rejected: self.__catch__(self.error)
        # Preset Triggers
        self.then(lambda v: None)
        self.catch(lambda e: None)
        # Set Thread
        super().__init__(self.__caller__, start=start, log=False)

    # Resolve Method
    def __resolve__(self, value):
        super().__resolve__(value)
        raise Exception(value)

    # Reject Method
    def __reject__(self, error):
        super().__reject__(error)
        raise Exception(error)

    @property
    def args(self):
        return list((self.__resolve__,
            self.__reject__))

    @property
    def kwargs(self):
        return dict(resolve = self.__resolve__,
            reject = self.__reject__)

    # Then Trigger
    def then(self, function):
        return self.__settrig__(function, True)

    # Catch Trigger
    def catch(self, function):
        return self.__settrig__(function, False)

    # Set Trigger
    def __settrig__(self, function, resolve):
        # Nest Objects
        if not callable(function): return None
        function = call.Safe(function)
        if resolve: self.__then__ = function
        else: self.__catch__ = function
        # Return Thread
        return function

    # Promise Wait
    def wait(self):
        # Check If Thread Is Done
        while not self.done: pass
        # Return Resolution
        return self.resolution
    
##########################################################################################################################
