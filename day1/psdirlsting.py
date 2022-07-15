__author__ = 'ravi'
from sys import argv
from glob import glob
from os import stat
from os.path import join, basename
from pprint import pprint
from pickle import dump

def directory_listing(*directories):
    content = {}
    file_glob = directories[-1]
    for directory_name in directories[:-1]:
        abs_path = join(directory_name, file_glob)
        for abs_file_name in glob(abs_path):
            f_name = basename(abs_file_name)
            content.setdefault(directory_name, {})[f_name] = \
                        stat(abs_file_name).st_size
    return content


content = directory_listing(*argv[1:])
dump(content, open('fileglob.dat', 'w'))
pprint(content)