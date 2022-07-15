__author__ = 'ravi'
from sys import argv, exc_info
from traceback import  print_tb

def safe_float(value):
    try:
        print "above to the return"
        return float(value[1])
        print "below to the return"

    except ValueError, e:
        print e
    except (IndexError, KeyError), e:
        print e
        print e.__class__
    except:
        """
        print "internal server error"
        print exc_info()[0]
        print exc_info()[1]
        """
        print print_tb(exc_info()[2])
    finally:
        print "finally block of exception handling"

print safe_float(argv)

