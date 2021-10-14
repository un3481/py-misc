
##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################

# Import Miscelllaneous
from ..py_misc import threading

# Import Threading Classes
from ._daemon import Daemon
from ._promise import Promise
from ._async import Async
from ._cycle import Cycle
from ._serial import Serial

##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################

# Promise Wait All
def wait_all(promises):
    while not all(i.done for i in promises): pass
    return list(map(lambda i: i.resolution, promises))

# Current Thread is Main
def is_main():
    cur = threading.current_thread()
    main = threading.main_thread()
    return cur is main

##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################
