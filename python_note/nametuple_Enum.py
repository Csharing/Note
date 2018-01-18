from functools import namedtuple

row=['a','b']

ki=namedtuple('k',row)

s=ki('j','l')

print(s.a)

from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.__members__)

@unique
class weekday(Enum):
    __a=1
    b=2
    c=3

class day():
    a=1
    b=2
    c=3

a=weekday
b=day()

print(type(a.__a))


