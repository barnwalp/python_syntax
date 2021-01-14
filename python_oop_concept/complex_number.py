import math
import copy

class Complex(object):
    def __init__(self, real, imaginary):
       self.real = real
       self.imaginary = imaginary

    def __add__(self, no):
        new = copy.copy(self)
        new.real = self.real + no.real
        new.imaginary = self.imaginary + no.imaginary
        return new.__str__()
        #return "%.2f+%.2fi" % (self.real+no.real, self.imaginary+no.imaginary)

    def __sub__(self, no):
        new = copy.copy(self)
        new.real = self.real - no.real
        new.imaginary = self.imaginary - no.imaginary
        return new.__str__()
        """
        if (self.imaginary - no.imaginary) >= 0:
            return "%.2f+%.2fi" % (self.real-no.real, self.imaginary-no.imaginary)
        else:
            return "%.2f%.2fi" % (self.real-no.real, self.imaginary-no.imaginary)
        """

    def __mul__(self, no):
        new = copy.copy(self)
        new.real = (self.real*no.real)-(self.imaginary*no.imaginary)
        new.imaginary = (self.real*no.imaginary)+(self.imaginary*no.real)
        return new.__str__()
        """
        if b > 0:
            return "%.2f+%.2fi" % (a, b)
        elif b < 0:
            return "%.2f%.2fi" % (a, b)
        else:
            return "%.2f" % (a)
        """

    def __truediv__(self, no):
        conj_no = copy.copy(no)
        new = copy.copy(no)
        conj_no.real = no.real
        conj_no.imaginary = no.imaginary-2*no.imaginary
        a = self.__mul__(conj_no)
        print(f'complex number a is: {a}')
        b = no.__mul__(conj_no)
        denm = b.split('+')[0]
        #print(f'b is: {denm}')
        if len(a.split('+')) == 2:
            r, i = a.split('+')
            i = i[:-1]
        elif len(a.split('-')) == 2:
            r, i = a.split('-')
            i = -float(i[:-1])
        elif len(a.split('-')) > 2:
            temp, r, i = a.split('-')
            r = -float(r)
            i = -float(i[:-1])

        #print(f'r is: {r} and i is: {i}')
        if not float(denm) == 0.00:
            new.real = float(r)/float(denm)
            new.imaginary = float(i)/float(denm)
        return new.__str__()

    def mod(self):
        new = copy.copy(self)
        new.real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        new.imaginary = 0.00
        return new.__str__()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    str_1 = input("Enter two numbers: ")
    print(str_1)
    str_2 = input("Enter two numbers again: ")
    print(str_2)
    c = map(float, str_1.split())
    d = map(float, str_2.split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
