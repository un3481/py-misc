##########################################################################################################################
#                                                          SCHEDULE                                                      #
##########################################################################################################################

        # Each Class
        class Each(Misc):

            # Properties
            @property
            def one(self): return self.Every(1)
            @property
            def two(self): return self.Every(2)
            @property
            def three(self): return self.Every(3)
            @property
            def four(self): return self.Every(4)
            @property
            def five(self): return self.Every(5)
            @property
            def six(self): return self.Every(6)
            @property
            def seven(self): return self.Every(7)
            @property
            def eight(self): return self.Every(8)
            @property
            def nine(self): return self.Every(9)
            @property
            def ten(self): return self.Every(10)

            # Every Class
            class Every(Misc):

                # Init Every
                def __init__(self, step):
                    self.step = step

                @property
                def schedule(self): return self.misc.schedule
                @property
                def every(self): return self.schedule.every(self.step)
                @property
                def second(self): return self.Period('second', self.every)
                @property
                def seconds(self): return self.Period('seconds', self.every)
                @property
                def minute(self): return self.Period('minute', self.every)
                @property
                def minutes(self): return self.Period('minutes', self.every)
                @property
                def hour(self): return self.Period('hour', self.every)
                @property
                def hours(self): return self.Period('hours', self.every)
                @property
                def day(self): return self.Period('day', self.every)
                @property
                def days(self): return self.Period('days', self.every)
                @property
                def week(self): return self.Period('week', self.every)
                @property
                def weeks(self): return self.Period('weeks', self.every)

                # Period Class
                class Period(Misc):

                    # Init Period
                    def __init__(self, period, every):
                        self.period = period
                        self.every = every

                    @property
                    def do(self):
                        return self.Do(self.period, self.every)

                    # Do Class
                    class Do(Misc):

                        # Init Do
                        def __init__(self, period, every):
                            self.period = period
                            self.every = every

                        @property
                        def __act__(self):
                            return getattr(self.every, self.period)

                        # Do At
                        def at(self, time):
                            def __decorator__(function):
                                if not callable(function): return False
                                function = self.misc.call.safe(function)
                                fasync = self.misc.threading.Async(function)
                                self.__act__.at(time).do(fasync)
                                return function
                            return __decorator__

                        # Do
                        def __call__(self, function):
                            if not callable(function): return False
                            function = self.misc.call.safe(function)
                            fasync = self.misc.threading.Async(function)
                            self.__act__.do(fasync)
                            return function
