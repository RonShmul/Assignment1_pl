import math


class ComplexNum:
    def __init__(self, a=0, b=0):  # todo: check the input? what are the possibilities- int, float..?
        self.a = a
        self.b = b

    def __repr__(self):
        if str(self.b).startswith('-'):
            return str(self.a) + ' - ' + str(self.b).replace('-', '') + 'i'
        return str(self.a) + ' + ' + str(self.b) + 'i'

    def __eq__(self, other):
        if isinstance(other, ComplexNum):
            return self.a == other.a and self.b == other.b
        return False

    def __add__(self, other):
        if isinstance(other, ComplexNum):  # todo: do we need to support add int,float?
            return ComplexNum(self.a+other.a, self.b+other.b)
        return False

    def __neg__(self):
        return ComplexNum(-self.a, -self.b)

    def __sub__(self, other):
        if isinstance(other, ComplexNum):  # todo: same as add(?)
            return self+(-other)
        return False

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
        raise TypeError('Complex multiplication only defined for Complex Numbers')

    def re(self):
        return self.a

    def im(self):
        return self.b  # todo: needs to be with i?

    def to_tuple(self):
        return self.re(), self.im()  # todo: return mamashi, merucav or mamashi,medume????

    def conjugate(self):
        return ComplexNum(self.a, -self.b)

    def __abs__(self):
        return math.sqrt((self*(self.conjugate())).a)


def isInstancePPL(object1, classInfo):
    pass

x1 = ComplexNum(-1, -5)
x2 = ComplexNum(4, -6)
x3 = ComplexNum(-1, -5)
x4 = ComplexNum(2, 2)
x5 = -x2
x6 = x2+x1
x7 = ComplexNum(0, 0)
x8 = x2-x7
x9 = x4*ComplexNum(1, 1)
x10 = x5.conjugate()
print(x1*x1.conjugate())
print(x5)
print(x10)
print(x9)
print(x2 == ComplexNum(4, -6))
