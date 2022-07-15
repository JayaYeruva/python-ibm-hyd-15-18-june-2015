__author__ = 'ravi'

class Box(object):
    def __init__(self, size):
        self.size = size

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Box(self.size * other)
        elif type(other) == Box:
            return Box(self.size * other.size)

    __rmul__ = __mul__

    def __add__(self, other):
        return Box(self.size + other.size)

    def __repr__(self):
        return "<{} size={}>".format(self.__class__.__name__, self.size)

    def __str__(self):
        return "[{} size={}]".format(self.__class__.__name__, self.size)


if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(11)
    b3 = b1 + b2  #b1.__add__(b2)
    print 3 * b3