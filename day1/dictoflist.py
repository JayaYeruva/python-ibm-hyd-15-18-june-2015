__author__ = 'ravi'
from pprint import pprint
ul = {l.split(':')[0]: l.rstrip().split(':')[1:]
                        for l in open('/etc/passwd') }

def sort_key(key):

    return int(ul[key][1])


for login in sorted(ul, key=sort_key):

    temp = ul[login]
    print "{}:{}:{}".format(temp[1], login, temp[-1])


