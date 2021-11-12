
##########################################################################################################################

# Imports
import flask
import flask_httpauth
import logging
from typing import Any, Callable as CallableType

# Modules
from . import misc
from . import call
from . import threading

##########################################################################################################################
#                                                            APP                                                         #
##########################################################################################################################

# Express Class
class Express(misc.Misc):

    # Init Server
    def __init__(self, log=True):
        # Check Parameters
        if not isinstance(log, bool):
            self = False
            return None
        
        # Define App
        self.__server__ = self.flask.Flask(__name__)

        # Remove Flask Logging
        if not log:
            self.__server__.logger.disabled = True
            logging.getLogger('werkzeug').disabled = True
        
        # Set Routes Dictionary
        self.__routes__ = dict()

        # Set Default Host
        self.__host__ = '0.0.0.0'

    @property
    def flask(self):
        return flask
    
    @property
    def httpauth(self):
        return flask_httpauth
   
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
            function: CallableType[[flask.Request, flask.Response], Any]
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
            self.__thread__ = threading.Daemon(
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
class Route(call.Callable):

    # Init Route
    def __init__(
        self,
        app: Express,
        function: CallableType[[flask.Request, flask.Response], Any],
        route: str,
        methods: list[str]
    ):
        # Check for Callable
        if (not callable(function) or
            not isinstance(route, str)):
            self = False
            return None
        
        # Set Callable
        self.__callable__ = call.Safe(function)

        # Set APP
        self.app = app
        self.__route__ = str(route)
        self.__auth__ = self.app.httpauth.HTTPBasicAuth()

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
            req = self.app.flask.request
            res = self.app.flask.Response
            return self.__callable__(req, res)
        
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
