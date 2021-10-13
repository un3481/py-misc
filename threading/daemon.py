##########################################################################################################################
#                                                          DAEMON                                                        #
##########################################################################################################################

        # Daemon Class
        class Daemon(Resolvable):

            # Init Daemon
            def __init__(self, function, start=True, log=True):

                # Check Parameters
                if (not callable(function) or
                    not isinstance(log, bool) or
                    not isinstance(start, bool)):
                    self = False
                    return None

                # Init Resolvable
                function = self.misc.call.safe(function, log)
                super().__init__(function, log)

                # Set Thread
                self.__thread__ = self.threading.Thread(target=self.__callable__)
                self.__thread__.daemon = True

                # Start Thread
                if start: self.start()

            @property
            def threading(self):
                return self.misc.threading

            @property
            def start(self):
                return self.__thread__.start

            @property
            def is_alive(self):
                return self.__thread__.is_alive

            @property
            def join(self):
                return self.__thread__.join

##########################################################################################################################
#                                                         PROMISE                                                        #
##########################################################################################################################

        # Promise Class
        class Promise(Daemon):

            # Init Promise
            def __init__(self, function, start=True):

                # Check Parameters
                if (not callable(function) or
                    not isinstance(start, bool)):
                    self = False
                    return None

                # Set Caller
                self.__caller__ = self.misc.call.caller(function, log=False)
                self.__caller__.__pass__ = True

                # Set Caller Arguments
                self.__caller__.setargs(*self.args, **self.kwargs)

                # Set Caller Call
                @self.__caller__.call
                def __promise__(obj):
                    obj.__callable__(*obj.args, **obj.kwargs)
                    if self.resolved: self.__then__(self.value)
                    elif self.rejected: self.__catch__(self.error)

                # Preset Triggers
                self.then(lambda v: None)
                self.catch(lambda e: None)

                # Set Thread
                super().__init__(self.__caller__, start=start, log=False)

            # Resolve Method
            def __resolve__(self, value):
                super().__resolve__(value)
                raise Exception(value)

            # Reject Method
            def __reject__(self, error):
                super().__reject__(error)
                raise Exception(error)

            @property
            def args(self):
                return list((self.__resolve__,
                    self.__reject__))

            @property
            def kwargs(self):
                return dict(resolve = self.__resolve__,
                    reject = self.__reject__)

            # Then Trigger
            def then(self, function):
                return self.__settrig__(function, True)

            # Catch Trigger
            def catch(self, function):
                return self.__settrig__(function, False)

            # Set Trigger
            def __settrig__(self, function, resolve):
                # Nest Objects
                if not callable(function): return None
                function = self.misc.call.safe(function)
                if resolve: self.__then__ = function
                else: self.__catch__ = function
                # Return Thread
                return function

            # Promise Wait
            def wait(self):
                # Check If Thread Is Done
                while not self.done: pass
                # Return Resolution
                return self.resolution

##########################################################################################################################
            
        # Promise Wait All
        def wait_all(promises):
            while not all(i.done for i in promises): pass
            return list(map(lambda i: i.resolution, promises))

##########################################################################################################################
#                                                           ASYNC                                                        #
##########################################################################################################################

        # Async Class
        class Async(Caller):

            # Init Async
            def __init__(self, function, log=False):

                # Check Parameters
                if (not callable(function) or
                    not isinstance(log, bool)):
                    self = False
                    return None

                # Init Caller
                super().__init__(function, log)

                # Caller to Promise
                @self.call
                def __promise__(obj):
                    __caller__ = self.misc.call.caller(obj.__callable__)
                    __caller__.__pass__ = True
                    __caller__.setargs(*obj.iargs, **obj.ikwargs)
                    return self.threading.promise(__caller__)

            @property
            def threading(self):
                return self.misc.threading

##########################################################################################################################
#                                                            CYCLE                                                       #
##########################################################################################################################

        # Cycle Thread Class
        class Cycle(Daemon):

            # Init Now
            def __init__(self, function, delay=None, start=True):

                # Check Parameters
                if (not callable(function) or
                    not isinstance(start, bool)):
                    self = False
                    return None

                # Set Cyclic Try
                self.__try__ = self.misc.call.Try(function=function)
                self.__try__.times(None).delay(delay).timeout(None)
                self.__try__.condition(lambda obj: False)

                # Set Thread Object
                super().__init__(self.__try__, start=start, log=False)

##########################################################################################################################
#                                                           SERIAL                                                       #
##########################################################################################################################

        # Instant Scheduler Class
        class Serial(Cycle):

            # Init Now
            def __init__(self, start=True):

                # Check Parameters
                if not isinstance(start, bool):
                    self = False
                    return None

                # Define Execution Series
                self.__queue__ = self.queue.Queue()

                # Set Thread Object
                super().__init__(self.__pending__, start)

            @property
            def queue(self):
                return self.misc.queue

            # Run Pending
            def __pending__(self):
                if not self.__queue__.empty():
                    promise = self.__queue__.get()
                    promise.start()
                    promise.wait()

            # Add Functions
            def add(self, function):
                # Check for Callable
                if not callable(function): return False
                function = self.threading.promise(function, False)
                self.__queue__.put(function)
                # Return Promise
                return function
