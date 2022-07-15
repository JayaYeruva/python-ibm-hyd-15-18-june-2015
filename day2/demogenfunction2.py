__author__ = 'ravi'


class Demo(object):
    pass

def yrange(start, stop):
    while start < stop:
        yield Demo()
        start += 1
        yield start

for i in yrange(1, 5):
    print i



