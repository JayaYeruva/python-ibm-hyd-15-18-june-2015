__author__ = 'ravi'

from sys import argv, stderr

def file_copy(source, dest):
    open(dest, 'w').write(open(source).read())

def usage():
    print >>stderr, "Usage:"
    print >>stderr,  "{} source-file dest-file".format(argv[0])
    exit(1)

if len(argv) != 3:
    usage()

file_copy(argv[1], argv[2])



