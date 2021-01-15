import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        new = copy(self)
        new.x = self.x - no.x
        new.y = self.y - no.y
        new.z = self.z - no.z
        return new

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        new = copy(self)
        new.x = self.y * no.z - self.z * no.y
        new.y = -(self.x * no.z - self.z * no.x)
        new.z = self.x * no.y - self.y * no.x
        return new

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    print('printing from main function')
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
    # In a function call, * unpacks a list of tuple into positional arguments
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    # since __sub__ function is overloaded, - can be used to subtract coordinates
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
