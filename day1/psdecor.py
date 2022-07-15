__author__ = 'ravi'

def arg_str_decor(message):
    def str_decor(func):
        def add_decor(*args, **kwargs):
            return "{}: [{}]".format(message, func(args[0]))

        return add_decor
    return str_decor

@arg_str_decor('a sample decor')
def demo(value):
    return value

print demo

#demo = str_decor(demo)

print demo('peter pan')

