
##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################

# Cyclic Reference
from .._time import Misc

##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################

# Delta Class
class Delta(Misc):

    # Init Delta
    def __init__(self):
        self.since = self.Since()

    # Reset Delta
    def reset(self): self.since.reset()

    # Since Class
    class Since(Misc):

        # Init Since
        def __init__(self): self.reset()

        # Reset Delta
        def reset(self):
            self.__start__ = self.misc.datetime.datetime.now()
            self.__last__ = self.misc.datetime.datetime.now()
            self.__delta__ = (self.__last__ - self.__start__)

        @property
        def init(self):
            self.__last__ = self.misc.datetime.datetime.now()
            return (self.__last__ - self.__start__)

        @property
        def last(self):
            now = self.misc.datetime.datetime.now()
            self.__delta__ = (now - self.__last__)
            self.__last__ = now
            return self.__delta__
        
##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################
