__author__ = 'ravi'
from sys import exc_info

class Connector(object):
    max_connection = 5
    counter = 0

    def __str__(self):
        return "{}:Connection id:{}".format(Connector.counter, self.connection_id)

    def __init__(self, connection_id):
        Connector.check_conection()
        Connector.counter += 1
        self.connection_id = connection_id

    @staticmethod
    def check_conection():
        if Connector.counter == Connector.max_connection:
            raise RuntimeError("max connection reached")


if __name__ == '__main__':
    conn = []
    try:
        for i in xrange(1, 8):
            conn.append(Connector("t"+str(i)))
    except:
        print exc_info()[0]
        print
        print exc_info()[1]
    finally:
        for c in conn:
            print c

    print Connector.counter
    print Connector.max_connection