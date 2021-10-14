
##########################################################################################################################
#                                                         RESOLVABLE                                                     #
##########################################################################################################################

# Cyclic Reference
from .._call import Callable

##########################################################################################################################
#                                                         RESOLVABLE                                                     #
##########################################################################################################################

# Resolvable Class
class Resolvable(Callable):

    # Init Resolvable
    def __init__(self, function, log=True):
        # Check Parameters
        if (not callable(function) or
            not isinstance(log, bool)):
            self = False
            return None
        # Init Callable
        super().__init__(function)
        # Set Status Attributes
        self.__resolved__ = False
        self.__rejected__ = False
        self.__value__ = None
        self.__error__ = None
        # Set Bypass
        self.__pass__ = True
        # Set Logging
        self.__log__ = None
        self.__logging__ = log

    @property
    def __bypass__(self):
        return (self.__pass__ and
            issubclass(self.__callable__.__class__, Resolvable))
    @property
    def resolved(self):
        return (self.__callable__.resolved
            if self.__bypass__ else self.__resolved__)
    @property
    def rejected(self):
        return (self.__callable__.rejected
            if self.__bypass__ else self.__rejected__)
    @property
    def value(self):
        return (self.__callable__.value
            if self.__bypass__ else self.__value__)
    @property
    def error(self):
        return (self.__callable__.error
            if self.__bypass__ else self.__error__)
    @property
    def done(self):
        return (self.resolved or self.rejected)
    @property
    def resolution(self):
        return (self.value if self.resolved else
            (self.error if self.rejected else None))

    # Resolve Method
    def __resolve__(self, value):
        if self.__bypass__:
            try: self.__callable__.__resolve__(value)
            except: pass
        self.__resolved__ = True
        self.__rejected__ = False
        self.__value__ = value
        self.__error__ = None
        # Return Value
        return self.value

    # Reject Method
    def __reject__(self, error):
        if self.__bypass__:
            try: self.__callable__.__reject__(error)
            except: pass
        self.__resolved__ = False
        self.__rejected__ = True
        self.__value__ = None
        self.__error__ = error
        self.__throw__()
        # Return Error
        return self.error

    # Reject Method
    def __reset__(self):
        if self.__bypass__:
            self.__callable__.__reset__()
        # Reset Status
        self.__resolved__ = False
        self.__rejected__ = False
        self.__value__ = None
        self.__error__ = None
        return True

    # Throw Error
    def __throw__(self):
        # Set Error Log
        self.__log__ = ('Throw(' + self.__locale__ + ') ' +
            'Catch(' + str(self.error) + ')')
        # Log Error
        self.__log__ = self.misc.log(self.__log__,
            self.__logging__, self.__logging__)
        # Return Log
        return self.__log__

##########################################################################################################################
#                                                         RESOLVABLE                                                     #
##########################################################################################################################
