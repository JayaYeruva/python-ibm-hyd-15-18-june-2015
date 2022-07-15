__author__ = 'ravi'

class Demo(object):
    def __init__(self):
        self.data = None

    def get_data(self):
        self.addr = '40 mg road'
        return self.data

if __name__ == '__main__':
    d = Demo('pypi')
    d = Demo()
    print d.get_data()
