
##########################################################################################################################
#                                                      MISCELLANEOUS                                                     #
##########################################################################################################################
       
# Imports
import os
import sys
import time
import flask
import flask_httpauth
import mysql.connector
import threading
import schedule

# Modules
from . import api
from . import call
from . import misc
from . import logs
from . import time as _time
from . import mysql as mysql
from . import threading as _threading
from . import schedule as _schedule

##########################################################################################################################
#                                                        NEST MODULES                                                    #
##########################################################################################################################

# Nest Reference Class
Misc = misc.Misc

# Nest Time Module
time.Delta = _time.Delta

# Nest Threading Module
threading.Cycle = _threading.Cycle
threading.Async = _threading.Async
threading.Serial = _threading.Serial
threading.Daemon = _threading.Daemon
threading.Promise = _threading.Promise

# Instance Log Class
log = logs.Logs()

# Import MySQL Module
MySQL = mysql.MySQL

# Import API Module
API = api.API

# Nest Schedule Module
schedule.each = _schedule.Each()
schedule.__thread__ = threading.Cycle(
    schedule.run_pending, delay=1
)

# Nest Flask Http-Auth Module
flask.httpauth = flask_httpauth

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
