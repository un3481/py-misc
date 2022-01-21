
##########################################################################################################################

# Imports
from schedule import *
from typing import Callable, Any

# Modules
from .threading import Async, Cycle

##########################################################################################################################

# Each Class
class Each:
    @property
    def one(self): return EachPeriod(1)
    @property
    def two(self): return EachPeriod(2)
    @property
    def three(self): return EachPeriod(3)
    @property
    def four(self): return EachPeriod(4)
    @property
    def five(self): return EachPeriod(5)
    @property
    def six(self): return EachPeriod(6)
    @property
    def seven(self): return EachPeriod(7)
    @property
    def eight(self): return EachPeriod(8)
    @property
    def nine(self): return EachPeriod(9)
    @property
    def ten(self): return EachPeriod(10)
    @property
    def eleven(self): return EachPeriod(11)
    @property
    def twelve(self): return EachPeriod(12)
    @property
    def thirteen(self): return EachPeriod(13)
    @property
    def fourteen(self): return EachPeriod(14)
    @property
    def fifteen(self): return EachPeriod(15)
    @property
    def sixteen(self): return EachPeriod(16)
    @property
    def seventeen(self): return EachPeriod(17)
    @property
    def eighteen(self): return EachPeriod(18)
    @property
    def nineteen(self): return EachPeriod(19)
    @property
    def twenty(self): return EachPeriod(20)
    @property
    def twentyOne(self): return EachPeriod(21)
    @property
    def twentyTwo(self): return EachPeriod(22)
    @property
    def twentyThree(self): return EachPeriod(23)
    @property
    def twentyFour(self): return EachPeriod(24)
    @property
    def twentyFive(self): return EachPeriod(25)
    @property
    def twentySix(self): return EachPeriod(26)
    @property
    def twentySeven(self): return EachPeriod(27)
    @property
    def twentyEight(self): return EachPeriod(28)
    @property
    def twentyNine(self): return EachPeriod(29)
    @property
    def thirty(self): return EachPeriod(30)
    @property
    def thirtyOne(self): return EachPeriod(31)
    @property
    def thirtyTwo(self): return EachPeriod(32)
    @property
    def thirtyThree(self): return EachPeriod(33)
    @property
    def thirtyFour(self): return EachPeriod(34)
    @property
    def thirtyFive(self): return EachPeriod(35)
    @property
    def thirtySix(self): return EachPeriod(36)
    @property
    def thirtySeven(self): return EachPeriod(37)
    @property
    def thirtyEight(self): return EachPeriod(38)
    @property
    def thirtyNine(self): return EachPeriod(39)
    @property
    def forty(self): return EachPeriod(40)
    @property
    def fortyOne(self): return EachPeriod(41)
    @property
    def fortyTwo(self): return EachPeriod(42)
    @property
    def fortyThree(self): return EachPeriod(43)
    @property
    def fortyFour(self): return EachPeriod(44)
    @property
    def fortyFive(self): return EachPeriod(45)
    @property
    def fortySix(self): return EachPeriod(46)
    @property
    def fortySeven(self): return EachPeriod(47)
    @property
    def fortyEight(self): return EachPeriod(48)
    @property
    def fortyNine(self): return EachPeriod(49)
    @property
    def fifty(self): return EachPeriod(50)
    @property
    def fiftyOne(self): return EachPeriod(51)
    @property
    def fiftyTwo(self): return EachPeriod(52)
    @property
    def fiftyThree(self): return EachPeriod(53)
    @property
    def fiftyfour(self): return EachPeriod(54)
    @property
    def fiftyFive(self): return EachPeriod(55)
    @property
    def fiftySix(self): return EachPeriod(56)
    @property
    def fiftySeven(self): return EachPeriod(57)
    @property
    def fiftyEight(self): return EachPeriod(58)
    @property
    def fiftyNine(self): return EachPeriod(59)
    @property
    def sixty(self): return EachPeriod(60)

##########################################################################################################################

# Every Class
class EachPeriod:
    def __init__(self, step: int):
        self.step = step
    @property
    def second(self): return EachPeriodDuration('second', self.step)
    @property
    def seconds(self): return EachPeriodDuration('seconds', self.step)
    @property
    def minute(self): return EachPeriodDuration('minute', self.step)
    @property
    def minutes(self): return EachPeriodDuration('minutes', self.step)
    @property
    def hour(self): return EachPeriodDuration('hour', self.step)
    @property
    def hours(self): return EachPeriodDuration('hours', self.step)
    @property
    def day(self): return EachPeriodDuration('day', self.step)
    @property
    def days(self): return EachPeriodDuration('days', self.step)
    @property
    def week(self): return EachPeriodDuration('week', self.step)
    @property
    def weeks(self): return EachPeriodDuration('weeks', self.step)

##########################################################################################################################

# Period Class
class EachPeriodDuration:
    # Init Period
    def __init__(self, period: str, step: int):
        self.every = every(step)
        self.period = period
    
    @property
    def do(self):
        return EachPeriodDo(self.period, self.every)

##########################################################################################################################

# Do Class
class EachPeriodDo:
    # Init Do
    def __init__(self, period: str, every):
        self.period = period
        self.every = every
    @property
    def __act__(self):
        return getattr(self.every, self.period)
    # Do At
    def at(self, time: str):
        def __decorator__(function: Callable[[], Any]):
            if not callable(function): return None
            fasync = Async(function)
            self.__act__.at(time).do(fasync)
            return function
        return __decorator__
    # Do
    def __call__(self, function):
        if not callable(function): return None
        fasync = Async(function)
        self.__act__.do(fasync)
        return function

##########################################################################################################################

# Instance Each
each = Each()

# Init Global Daemon Thread
__thread__ = Cycle(
    run_pending, delay=1
)

##########################################################################################################################
