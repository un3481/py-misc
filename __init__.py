
##########################################################################################################################
#                                                      MISCELLANEOUS                                                     #
##########################################################################################################################
       
# Imports
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

# Nest Miscellaneous Objects
self.json = json
self.copy = copy
self.time = time
self.typing = typing
self.pathlib = pathlib
self.random = random
self.requests = requests
self.flask = flask
self.flask.httpauth = flask_httpauth
self.logging = logging
self.queue = queue
self.threading = threading
self.schedule = schedule
self.dataclasses = dataclasses
self.unicodedata = unicodedata
self.unidecode = unidecode
self.datetime = datetime
self.builtins = builtins
self.inspect = inspect
self.signal = signal
self.sys = sys
self.os = os
self.re = re

##########################################################################################################################
#                                                        FIX IMPORTS                                                     #
##########################################################################################################################

# Fix MySQL Connector
class __mysql__:
    def __init__(self):
        self.__connector__ = mysql.connector
    @property
    def connector(self):
        return self.__connector__
# Nest Objects
self.__mysql__ = __mysql__()

##########################################################################################################################
#                                                         REFERENCE                                                      #
##########################################################################################################################

# Reference to Miscellaneous
class Misc:
    @property
    def misc(self): return misc
    @property
    def __locale__(self):
        return self.misc.locale(self)

        # Time Delta
        self.time.delta = self.construct(Delta)

        # Call
        import call
        self.call.callable = self.construct(Callable)
        self.call.safe = self.construct(Safe)
        self.call.caller = self.construct(Caller)
        self.call.Try = self.construct(Try)

        # Threading
        self.threading.daemon = self.construct(Daemon)
        self.threading.promise = self.construct(Promise)
        self.threading.Async = self.construct(Async)
        self.threading.wait_all = wait_all
        self.threading.cycle = self.construct(Cycle)
        self.threading.serial = self.construct(Serial)
        self.threading.is_main = (
            lambda: self.threading.current_thread() is
            self.threading.main_thread()
        )

        # MySQL
        mysql = self.construct(MySQL)

        # Logging
        log = logs()

        # API
        self.api = self.construct(API)

        # Schedule
        self.schedule.each = Each()
        self.schedule.__thread__ = self.threading.cycle(
            self.schedule.run_pending, delay=1
        )

##########################################################################################################################
#                                                       MISC METHODS                                                     #
##########################################################################################################################

    @property
    def misc(self): return self

    # Get Location of Main Script
    @property
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
