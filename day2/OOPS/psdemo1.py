__author__ = 'ravi'

class Demo(object):
    pass

if __name__ == '__main__':
    d = Demo()
    d.name = 'ibm'
    d.city = 'hyderabad'
    print d.__dict__
    print d.__class__.__name__
    print Demo
    print isinstance(d, Demo)
    print issubclass(Demo, object)
