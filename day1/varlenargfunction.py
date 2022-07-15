__author__ = 'ravi'

def demo(*args):
    print args

demo()
demo(1)
demo('peter')
demo(1, "pam", 3 ,4,5,65,7,7)

l = [1,2,3]
t = (6,7,8)
demo(*l)
demo(*t)