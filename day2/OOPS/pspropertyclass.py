__author__ = 'ravi'

class Property(object):
    def __init__(self):
        self.container = {}

    def __setitem__(self, key, value):
        self.container[key] = value

    def __getitem__(self, item):
        return self.container[item]

if __name__ == '__main__':
    p = Property()
    p['name'] = 'ibm'
    p['city'] = 'hyderabad'
    p['zip'] = 32124

    print p['name']
    print p['city']


