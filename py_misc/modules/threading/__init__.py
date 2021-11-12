
##########################################################################################################################

# Imports
import threading

# Modules
from . import cycle
from . import _async
from . import serial
from . import daemon
from . import promise

##########################################################################################################################

# Nest Classes
Cycle = cycle.Cycle
Async = _async.Async
Serial = serial.Serial
Daemon = daemon.Daemon
Promise = promise.Promise

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
