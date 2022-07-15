__author__ = 'ravi'

class RangeError(Exception):
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.message)

def check_limit(level):
    if level > 0.6:
        raise \
            RangeError("value beyond the allowable range: {}".format(level))

try:
    check_limit(.9)
except RangeError, e:
    print e

