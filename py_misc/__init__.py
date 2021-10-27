
##########################################################################################################################
#                                                      MISCELLANEOUS                                                     #
##########################################################################################################################
#                                                                                                                        #
#                                              Python Miscellaneous Library                                              #
#                                                    Author: Anthony                                                     #
#                                   -------------------- Python3 --------------------                                    #
#                                                 * Under Development *                                                  #
#                                      https://github.com/anthony-freitas/py-misc                                        #
#                                                                                                                        #
##########################################################################################################################
#                                                       MAIN CODE                                                        #
##########################################################################################################################

# Imports
import os
import sys
import time
import threading
import schedule

# Modules
from . import modules

##########################################################################################################################
#                                                        NEST MODULES                                                    #
##########################################################################################################################

# Nest Time Module
time.Delta = modules.time.Delta

# Nest Threading Module
threading.Cycle = modules.threading.Cycle
threading.Async = modules.threading.Async
threading.Serial = modules.threading.Serial
threading.Daemon = modules.threading.Daemon
threading.Promise = modules.threading.Promise

# Instance Log Class
log = modules.logs.Logs()

# Import MySQL Module
MySQL = modules.mysql.MySQL

# Import API Module
API = modules.api.API

# Nest Schedule Module
schedule.each = modules.schedule.Each()
schedule.__thread__ = threading.Cycle(
    schedule.run_pending, delay=1
)

##########################################################################################################################
#                                                       MISC METHODS                                                     #
##########################################################################################################################

# Get Location of Main Script
def __schema__():
    path = sys.modules['__main__'].__file__
    path = os.path.abspath(path)
    return path

# Get Reference Object
def proxy_reference(obj):
    reference = [obj]
    while hasattr(reference[-1], '__proxy__'):
        reference.append(reference[-1].__proxy__)
    return reference[-1]

# Get Location of Object in Script
def locale(obj):
    reference = proxy_reference(obj)
    module = reference.__module__ if hasattr(reference, '__module__') else '__main__'
    module = module if module.startswith('__main__') else '::'.join(('__main__', module))
    qual = reference.__qualname__ if hasattr(reference, '__qualname__') else '__?__'
    locale = '::'.join((module, qual))
    locale = locale.replace('.<locals>.', '::')
    return locale

# Keep Alive
def keepalive():
    try: # Keep Main Thread Alive
        while True: pass
    except KeyboardInterrupt: pass

##########################################################################################################################
#                                                           END                                                          #
##########################################################################################################################
