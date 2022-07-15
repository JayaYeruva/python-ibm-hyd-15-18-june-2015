__author__ = 'ravi'

def yrange():
    print "before yield 1"
    yield xrange(12)
    print "after yield 1"
    print "before yield 2"
    yield 'one'
    print "after yield 2"

g = yrange()
print g.next()
print g.next()


