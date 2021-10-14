
##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################

# Import Miscelllaneous
import .misc as misc

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
    cur = misc.threading.current_thread()
    main = misc.threading.main_thread()
    return cur is main

##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################
