
# Cyclic Reference
from call import Misc

##########################################################################################################################
#                                                            SAFE                                                        #
##########################################################################################################################

        # Safe Class
        class Safe(Resolvable):

            # Init Safe
            def __init__(self, function, log=True):
                # Init Resolvable
                super().__init__(function, log)

            # Call Method
            def __call__(self, *args, **kwargs):
                # Reset Values
                self.__reset__()
                # Check If Callable Is Resolvable
                if self.__bypass__:
                    # Execute Callable
                    try: value = self.__callable__(*args, **kwargs)
                    except: pass
                    # Fix Resolution
                    if self.done: return self.resolution
                    # Exchange Resolution
                    self.__resolved__ = self.__callable__.resolved
                    self.__rejected__ = self.__callable__.rejected
                    self.__value__ = self.__callable__.value
                    self.__error__ = self.__callable__.error
                    # Return Resolution
                    return self.resolution
                else: # If Callable Is Not Resolvable
                    try: # Execute Callable
                        value = self.__callable__(*args, **kwargs)
                        # Fix Resolution
                        if self.done: return self.resolution
                        # Handle Resolve
                        try: self.__resolve__(value)
                        except: pass
                        return self.resolution
                    # On Error
                    except Exception as error:
                        # Fix Resolution
                        if self.done: return self.resolution
                        # Handle Reject
                        try: self.__reject__(error)
                        except: pass
                        return self.resolution
                # If Else
                return None
