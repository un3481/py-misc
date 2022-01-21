
#################################################################################################################################################

# Imports
from typing import Literal, TypeVar, ParamSpec, Callable

#################################################################################################################################################

P = ParamSpec('P')
R = TypeVar('R')

Ok = tuple[Literal[True], R]
Err = tuple[Literal[False], Exception]
Return = Ok[R] | Err

UnsafeCallable = Callable[P, R]
SafeCallable = Callable[P, Return[R]]

def Safe(function: UnsafeCallable[P, R]) -> SafeCallable[P, R]:
    def __safe__(*args, **kwargs):
        try: return (True, function(*args, **kwargs))
        except Exception as error: return (False, error)
    return __safe__

#################################################################################################################################################
