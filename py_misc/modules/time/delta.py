
##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################

# Imports
import datetime

# Modules
from .. import misc

##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################

# Delta Class
class Delta(misc.Misc):

    # Init Delta
    def __init__(self):
        self.since = self.Since()

    # Reset Delta
    def reset(self): self.since.reset()

    # Since Class
    class Since(misc.Misc):

        # Init Since
        def __init__(self): self.reset()

        # Reset Delta
        def reset(self):
            self.__start__ = datetime.datetime.now()
            self.__last__ = datetime.datetime.now()
            self.__delta__ = (self.__last__ - self.__start__)

        @property
        def init(self):
            self.__last__ = datetime.datetime.now()
            return (self.__last__ - self.__start__)

        @property
        def last(self):
            now = datetime.datetime.now()
            self.__delta__ = (now - self.__last__)
            self.__last__ = now
            return self.__delta__
        
##########################################################################################################################
#                                                        DELTA TIME                                                      #
##########################################################################################################################
