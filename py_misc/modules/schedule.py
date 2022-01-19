
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
    def one(self): return Every(1)
    @property
    def two(self): return Every(2)
    @property
    def three(self): return Every(3)
    @property
    def four(self): return Every(4)
    @property
    def five(self): return Every(5)
    @property
    def six(self): return Every(6)
    @property
    def seven(self): return Every(7)
    @property
    def eight(self): return Every(8)
    @property
    def nine(self): return Every(9)
    @property
    def ten(self): return Every(10)
    @property
    def eleven(self): return Every(11)
    @property
    def twelve(self): return Every(12)
    @property
    def thirteen(self): return Every(13)
    @property
    def fourteen(self): return Every(14)
    @property
    def fifteen(self): return Every(15)
    @property
    def sixteen(self): return Every(16)
    @property
    def seventeen(self): return Every(17)
    @property
    def eighteen(self): return Every(18)
    @property
    def nineteen(self): return Every(19)
    @property
    def twenty(self): return Every(20)
    @property
    def twentyOne(self): return Every(21)
    @property
    def twentyTwo(self): return Every(22)
    @property
    def twentyThree(self): return Every(23)
    @property
    def twentyFour(self): return Every(24)
    @property
    def twentyFive(self): return Every(25)
    @property
    def twentySix(self): return Every(26)
    @property
    def twentySeven(self): return Every(27)
    @property
    def twentyEight(self): return Every(28)
    @property
    def twentyNine(self): return Every(29)
    @property
    def thirty(self): return Every(30)
    @property
    def thirtyOne(self): return Every(31)
    @property
    def thirtyTwo(self): return Every(32)
    @property
    def thirtyThree(self): return Every(33)
    @property
    def thirtyFour(self): return Every(34)
    @property
    def thirtyFive(self): return Every(35)
    @property
    def thirtySix(self): return Every(36)
    @property
    def thirtySeven(self): return Every(37)
    @property
    def thirtyEight(self): return Every(38)
    @property
    def thirtyNine(self): return Every(39)
    @property
    def forty(self): return Every(40)
    @property
    def fortyOne(self): return Every(41)
    @property
    def fortyTwo(self): return Every(42)
    @property
    def fortyThree(self): return Every(43)
    @property
    def fortyFour(self): return Every(44)
    @property
    def fortyFive(self): return Every(45)
    @property
    def fortySix(self): return Every(46)
    @property
    def fortySeven(self): return Every(47)
    @property
    def fortyEight(self): return Every(48)
    @property
    def fortyNine(self): return Every(49)
    @property
    def fifty(self): return Every(50)
    @property
    def fiftyOne(self): return Every(51)
    @property
    def fiftyTwo(self): return Every(52)
    @property
    def fiftyThree(self): return Every(53)
    @property
    def fiftyfour(self): return Every(54)
    @property
    def fiftyFive(self): return Every(55)
    @property
    def fiftySix(self): return Every(56)
    @property
    def fiftySeven(self): return Every(57)
    @property
    def fiftyEight(self): return Every(58)
    @property
    def fiftyNine(self): return Every(59)
    @property
    def sixty(self): return Every(60)

##########################################################################################################################

# Every Class
class Every:
    def __init__(self, step: int):
        self.step = step
    @property
    def second(self): return EachPeriod('second', self.step)
    @property
    def seconds(self): return EachPeriod('seconds', self.step)
    @property
    def minute(self): return EachPeriod('minute', self.step)
    @property
    def minutes(self): return EachPeriod('minutes', self.step)
    @property
    def hour(self): return EachPeriod('hour', self.step)
    @property
    def hours(self): return EachPeriod('hours', self.step)
    @property
    def day(self): return EachPeriod('day', self.step)
    @property
    def days(self): return EachPeriod('days', self.step)
    @property
    def week(self): return EachPeriod('week', self.step)
    @property
    def weeks(self): return EachPeriod('weeks', self.step)

##########################################################################################################################

# Period Class
class EachPeriod:
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
            if not callable(function): return False
            fasync = Async(function)
            self.__act__.at(time).do(fasync)
            return function
        return __decorator__
    # Do
    def __call__(self, function):
        if not callable(function): return False
        fasync = Async(function)
        self.__act__.do(fasync)
        return function

##########################################################################################################################

__thread__ = Cycle(
    run_pending, delay=1
)

##########################################################################################################################
