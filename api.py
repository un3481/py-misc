
##########################################################################################################################
#                                                            API                                                         #
##########################################################################################################################

# Imports
from py_misc import Misc
from _call import Callable

##########################################################################################################################
#                                                            API                                                         #
##########################################################################################################################

# API Class
class API(Misc):
    # Init API
    def __init__(self, log=True):
        # Check Parameters
        if not isinstance(log, bool):
            self = False
            return None
        # Define App
        self.__app__ = self.flask.Flask(__name__)
        # Remove Flask Logging
        if not log:
            self.__app__.logger.disabled = True
            self.misc.logging.getLogger('werkzeug').disabled = True
        # Set Routes Dictionary
        self.__routes__ = dict()
        # Set Server Params
        self.host(None).port(None)

    @property
    def flask(self):
        return self.misc.flask
    
    @property
    def httpauth(self):
        return self.misc.flask.httpauth
    
    # Set Host
    def host(self, host):
        self.__host__ = host
        return self
    
    # Set Port
    def port(self, port):
        self.__port__ = port
        return self
    
    # Route Class
    class Route(Callable):
        
        # Init Route
        def __init__(self, api, function, route, methods):
            # Check for Callable
            if (not callable(function) or
                not isinstance(route, str)):
                self = False
                return None
            
            # Set Callable
            self.__callable__ = self.misc.call.safe(function)
            # Set API
            self.__api__ = api
            self.__route__ = str(route)
            self.__auth__ = self.__api__.httpauth.HTTPBasicAuth()
            # Set Auth Params
            self.user(None).password(None)
            # Auth Verify
            @self.__auth__.verify_password
            def __auth__(user, password):
                a = (self.__user__ == user or
                    self.__user__ == None)
                b = (self.__password__ == password or
                    self.__password__ == None)
                if a and b: return user
            # Create Dynamic Named Function
            def __route__():
                json = self.__api__.misc.copy.deepcopy(self.__api__.flask.request.json)
                data = self.__callable__(json)
                return self.__api__.flask.jsonify(data)
            __route__.__name__ = route.replace('/','_')
            # Route Flask App
            self.__api__.__app__.route(self.__route__, methods=methods)(
                self.__auth__.login_required(__route__)
            )

        # Set User
        def user(self, user):
            self.__user__ = user
            return self

        # Set Password
        def password(self, password):
            self.__password__ = password
            return self
    
    # Add Route to App
    def add(self, route, methods=['GET', 'POST']):
        def __decorator__(function):
            if (not callable(function) or
                not isinstance(route, str)): return False
            __route__ = self.Route(self, function, route, methods)
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
            self.__thread__ = self.misc.threading.daemon(
                lambda: self.__app__.run(host=self.__host__, port=self.__port__)
            )
        except: return False
        # Return True
        return True