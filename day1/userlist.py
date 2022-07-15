__author__ = 'ravi'

from pprint import pprint

ul = sorted([l.split(':')[0].upper()
             for l in open('/etc/passwd') if l.startswith('a')])

for i, login in enumerate(ul, 1):
    print "{:>6}  {}".format(i, login)

