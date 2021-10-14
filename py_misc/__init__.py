
##########################################################################################################################
#                                                      MISCELLANEOUS                                                     #
##########################################################################################################################
       
# Generic Imports
import json
import copy
import time
import typing
import pathlib
import random
import requests
import flask
import flask_httpauth
import logging
import queue
import threading
import schedule
import dataclasses
import mysql.connector
import unicodedata
import unidecode
import datetime
import builtins
import inspect
import signal
import sys
import os
import re

##########################################################################################################################
#                                                         REFERENCE                                                      #
##########################################################################################################################

# Nest Flask Http-Auth Module
flask.httpauth = flask_httpauth

# Import Time Module
from ._time import Delta

# Nest Time Module
time.Delta = Delta

# Import Call Module
import ._call as call

# Import Threading Module
from ._threading import Daemon
from ._threading import Promise
from ._threading import Async
from ._threading import Cycle
from ._threading import Serial

# Nest Threading Module
threading.Daemon = Daemon
threading.Promise = Promise
threading.Async = Async
threading.Cycle = Cycle
threading.Serial = Serial

# Import Logs Module
from .logs import Logs

# Import MySQL Module
from .mysql import MySQL

# Import API Module
from .api import API

# Import Schedule Module
from .schedule import Each

# Nest Schedule Module
schedule.each = Each()
schedule.__thread__ = threading.Cycle(
    schedule.run_pending, delay=1
)

# Import Misc Reference Class
from .misc import Misc

##########################################################################################################################
#                                                       MISC METHODS                                                     #
##########################################################################################################################

# Get Location of Main Script
def __schema__(self):
    path = self.sys.modules['__main__'].__file__
    path = self.os.path.abspath(path)
    return path

# Get Reference Object
def proxy_reference(self, obj):
    reference = [obj]
    while hasattr(reference[-1], '__proxy__'):
        reference.append(reference[-1].__proxy__)
    return reference[-1]

# Get Location of Object in Script
def locale(self, obj):
    reference = self.proxy_reference(obj)
    module = reference.__module__ if hasattr(reference, '__module__') else '__main__'
    module = module if module.startswith('__main__') else '::'.join(('__main__', module))
    qual = reference.__qualname__ if hasattr(reference, '__qualname__') else '__?__'
    locale = '::'.join((module, qual))
    locale = locale.replace('.<locals>.', '::')
    return locale

# Keep Alive
def keepalive(self):
    try: # Keep Main Thread Alive
        while True: pass
    except KeyboardInterrupt: pass

##########################################################################################################################
#                                                           END                                                          #
##########################################################################################################################
