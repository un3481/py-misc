
##########################################################################################################################

# Imports
from logging import getLogger
from flask import Flask, Response, Request, request
from flask_httpauth import HTTPBasicAuth
from typing import Any, Callable

# Modules
from .call import Safe, Callable as CallableClass
from .threading import Daemon

##########################################################################################################################
#                                                            APP                                                         #
##########################################################################################################################

# Express Class
class Express:

    # Init Server
    def __init__(self, log=True):
        # Check Parameters
        if not isinstance(log, bool):
            self = False
            return None
        
        # Define App
        self.__server__ = Flask(__name__)

        # Remove Flask Logging
        if not log:
            self.__server__.logger.disabled = True
            getLogger('werkzeug').disabled = True
        
        # Set Routes Dictionary
        self.__routes__ = dict()

        # Set Default Host
        self.__host__ = '0.0.0.0'
   
    # Set Host
    def host(self, host: str):
        self.__host__ = host
        return self
    
    # Set Port
    def port(self, port: int):
        self.__port__ = port
        return self
    
    # Add Route to App
    def route(
        self,
        route: str,
        methods: list[str] = ['GET', 'POST']
    ):
        def __decorator__(
            function: Callable[[Request, Response], Any]
        ):
            if (not callable(function) or
                not isinstance(route, str)): return False
            __route__ = Route(self, function, route, methods)
            self.__routes__[route] = __route__
            return __route__
        # Return Decorator
        return __decorator__
    
    # Start App
    def start(self):
        # Check for Host and Port
        if (self.__host__ == None or
            self.__port__ == None): return False
        try: # Start Server on Daemon Thread
            self.__thread__ = Daemon(
                lambda: self.__server__.run(
                    host=self.__host__,
                    port=self.__port__
                )
            )
        except: return False
        # Return True
        return True

##########################################################################################################################
    
# Route Class
class Route(CallableClass):

    # Init Route
    def __init__(
        self,
        app: Express,
        function: Callable[[Request, Response], Any],
        route: str,
        methods: list[str]
    ):
        # Check for Callable
        if (not callable(function) or
            not isinstance(route, str)):
            self = False
            return None
        
        # Set Callable
        self.__callable__ = Safe(function)

        # Set APP
        self.app = app
        self.__route__ = str(route)
        self.__auth__ = HTTPBasicAuth()

        # Set Users
        self.users: dict[str, str] = dict()

        # Auth Verify
        @self.__auth__.verify_password
        def __auth__(user: str, password: str):
            # If No User Set
            if not self.users: return user
            if user not in self.users: return
            if password != self.users[user]: return
            else: return user
        
        # Create Dynamic Named Function
        def __route__():
            return self.__callable__(request, Response)
        
        # Set Dynamic Route Name
        __route__.__name__ = route.replace('/','_')

        # Route Flask App
        self.app.__server__.route(
            self.__route__,
            methods=methods
        )(
            self.__auth__.login_required(__route__)
        )
    
##########################################################################################################################
