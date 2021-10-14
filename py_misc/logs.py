
##########################################################################################################################
#                                                           LOGS                                                         #
##########################################################################################################################

# Imports
from py_misc import Misc

##########################################################################################################################
#                                                           LOGS                                                         #
##########################################################################################################################

# Logs Class
class Logs(Misc):

    # Init Logs
    def __init__(self, mysqlconn=None):
        # Set Constructor
        self.__constructor__ = self.misc.construct(self.Log)
        # Append Object
        if mysqlconn: self.mysql = mysqlconn
        else: self.mysql = None
    
    # Set SQL Connection
    def sqlconn(self, mysqlconn):
        self.mysql = mysqlconn
        return True

    # Log Class
    class Log(Misc):

        # Init Log
        def __init__(self, log, console=True, mysql=True):
            # Check Parameters
            if (not isinstance(log, str) or
                not isinstance(mysql, bool) or
                not isinstance(console, bool)):
                self = False
                return None
            # Get Timestamp
            self.__timestamp__ = self.misc.datetime.datetime.now()
            self.__log__ = self.misc.copy.deepcopy(log)
            # Execute
            if self.logs.mysql == None: mysql = False
            if self.logs.mysql and not self.logs.mysql.conn: mysql = False
            if mysql: self.__mysql__()
            if console: self()

        @property
        def logs(self):
            return self.misc.log

        @property 
        def __t__(self):
            t = self.__timestamp__
            t =  t.strftime('%m/%d/%Y, %H:%M:%S')
            t = '({})'.format(t)
            return t

        @property
        def __error__(self):
            if self.logs.mysql == None: return ''
            if self.logs.mysql.conn: return ''
            else: return '(MySQL Error)'

        # Log to MySQL
        def __mysql__(self):
            if self.logs.mysql == None: return None
            query = 'INSERT INTO logs (Timestamp, App, Log) VALUES (%s, %s, %s)'
            schema = self.misc.__schema__
            val = (self.__timestamp__, schema, self.__log__)
            e = self.logs.mysql.execute(query, val)
            return e

        # String Representation
        def __str__(self):
            strin = ' '.join((self.__t__,
                self.__log__, self.__error__))
            strin = strin.strip()
            return strin

        # Caller to Console Log
        def __call__(self):
            print(str(self))

    # Instance Object
    def __call__(self, *args, **kwargs):
        return self.__constructor__(*args, **kwargs)
    
##########################################################################################################################
#                                                           LOGS                                                         #
##########################################################################################################################
