
##########################################################################################################################

# Imports
from time import *
from datetime import datetime

##########################################################################################################################

# Delta Class
class Delta:
    # Init Delta
    def __init__(self):
        self.since = Since()
    # Reset Delta
    def reset(self): self.since.reset()

# Since Class
class Since:
    # Init Since
    def __init__(self): self.reset()
    # Reset Delta
    def reset(self):
        self.__start__ = datetime.now()
        self.__last__ = datetime.now()
        self.__delta__ = (self.__last__ - self.__start__)
    @property
    def init(self):
        self.__last__ = datetime.now()
        return (self.__last__ - self.__start__)
    @property
    def last(self):
        now = datetime.now()
        self.__delta__ = (now - self.__last__)
        self.__last__ = now
        return self.__delta__

##########################################################################################################################
