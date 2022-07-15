__author__ = 'ravi'

class yrange(object):
    def __init__(self, stop):
        self.start = -1
        self.stop = stop

    def __iter__(self):
        print "mocking it as iter"
        return self

    def next(self):
        if self.start == self.stop-1:
            raise StopIteration
        self.start += 1
        return self.start

if __name__ == '__main__':
    for i in yrange(4):
        print i

    #yr = yrange(2)
    #yi =  iter(yr)
    #print yr
    #print yi
    #print yi.next()
    #print yi.next()
    #print yi.next()
