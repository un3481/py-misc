
##########################################################################################################################

# Import
import queue

# Modules
from .promise import Promise
from .cycle import Cycle

##########################################################################################################################
#                                                           SERIAL                                                       #
##########################################################################################################################

# Instant Scheduler Class
class Serial(Cycle):

    # Init Now
    def __init__(self, start=True):
        # Check Parameters
        if not isinstance(start, bool):
            self = False
            return None
        # Define Execution Series
        self.__queue__ = self.queue.Queue()
        # Set Thread Object
        super().__init__(self.__pending__, start)

    @property
    def queue(self):
        return queue

    # Run Pending
    def __pending__(self):
        if not self.__queue__.empty():
            promise = self.__queue__.get()
            promise.start()
            promise.wait()

    # Add Functions
    def add(self, function):
        # Check for Callable
        if not callable(function): return False
        function = Promise(function, False)
        self.__queue__.put(function)
        # Return Promise
        return function
    
##########################################################################################################################
