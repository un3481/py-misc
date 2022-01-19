
##########################################################################################################################

# Imports
from threading import *

# Modules
from .cycle import Cycle
from .caller import Async
from .serial import Serial
from .daemon import Daemon
from .promise import Promise

##########################################################################################################################

# Promise Wait All
def wait_all(promises):
    while not all(i.done for i in promises): pass
    return list(map(lambda i: i.resolution, promises))

# Current Thread is Main
def is_main():
    cur = current_thread()
    main = main_thread()
    return cur is main

##########################################################################################################################
