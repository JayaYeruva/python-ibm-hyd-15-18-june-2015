__author__ = 'ravi'

n = 100 #global

def demo():
    global n  #refer global version in
    n = 'pypi'   #local to function
    print locals()
    print n
    return "-" * 4



#print globals()
demo()
print n
print __name__  #namespace
print __file__

