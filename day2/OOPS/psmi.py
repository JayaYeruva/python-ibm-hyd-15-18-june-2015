__author__ = 'ravi'
class Prime(object):
    def pprint(self):
        print "pprint from the Prime"


class Zero(object):
    def pprint(self):
        print "pprint from class Zero"


class A(Zero, Prime):
    def pprint(self):
        print "pprint from the class A"
        super(A, self).pprint()

class B(Zero, Prime):
    def pprint(self):
        print "pprint from the class B"
        self.test()
        super(B, self).pprint()

    def test(self):
        print "test in the class B"

class C(B, A):
    def pprint(self):
        print "pprint in class c"
        super(C, self).pprint()

    def test(self):
        print "test in the class C"


if __name__ == '__main__':
    C().pprint()
    #b = B()
    #b.pprint()



