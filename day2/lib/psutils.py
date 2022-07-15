"""
a sample py module
"""
from os import listdir, getpid
import sys

name = 'ibm'
city = 'hyderabad'


def ls(path='.'):
    """
    ls() - list the directory content
    :param path: refers the path of the directory
    :return: None
    """
    for file_name in listdir(path):
        print file_name


def pid():
    """
    pid(), gets process id of the current process
    :return:
    """
    print "process id : {}".format(getpid())


class Dummy(object):
    """
    Dummy, the Dummy class
    """

    def get_version(self):
        """
        get_version(), gets the version and platform information of py
        :return:
        """
        print "version : {}".format(sys.version)
        print "platform : {}".format(sys.platform)


def main():
    print "namespace : {}".format(__name__)
    pid()
    d = Dummy()
    d.get_version()
    print name

if __name__ == '__main__':
    main()
