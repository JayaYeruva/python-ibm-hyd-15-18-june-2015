__author__ = 'ravi'
x = None

def demo1(platform):
    global  x
    if platform == 'linux2':
        x = 'yes'
    elif platform == 'win32':
        x = 'no'

def demo2():
    global x
    print x

demo1('win32')
demo2()

