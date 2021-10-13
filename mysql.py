##########################################################################################################################
#                                                           MySQL                                                        #
##########################################################################################################################

        # Class MySQL
        class MySQL(Misc):

            # Init MySQL
            def __init__(self, *args, **kwargs):

                # Set References
                self.args = args
                self.kwargs = kwargs

                # Start Thread
                self.__series__ = self.misc.threading.serial()

            @property
            def connector(self):
                return self.misc.__mysql__.connector

            @property
            def conn(self):
                try: # Check for mydb
                    mydb = self.__connect__()
                    conn = mydb.is_connected()
                    mydb.close()
                    return conn
                except: return False

            @property
            def mydb(self):
                if not self.conn: return False
                try: return self.__connect__()
                except: return False

            # Connect
            def __connect__(self):
                return self.connector.connect(*self.args, **self.kwargs)

            # Get Data From DB
            def get(self, query):
                @self.__series__.add
                def __fetch__(resolve, reject):
                    mydb = self.mydb
                    if mydb == False: reject(False)
                    cursor = mydb.cursor()
                    cursor.execute(query)
                    data = cursor.fetchall()
                    cursor.close()
                    mydb.close()
                    data = list(map(lambda i: list(i), list(data)))
                    if not isinstance(data, list): data = list()
                    resolve(data)
                # Return Resolution
                return __fetch__.wait()

            #  Execute Into DB
            def execute(self, query, val=tuple()):
                @self.__series__.add
                def __execute__(resolve, reject):
                    mydb = self.mydb
                    if mydb == False: reject(False)
                    cursor = mydb.cursor()
                    cursor.execute(query, val)
                    mydb.commit()
                    cursor.close()
                    mydb.close()
                    resolve(True)
                # Return Resolution
                return __execute__.wait()