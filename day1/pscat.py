__author__ = 'ravi'

from sys import argv


def cat(file_name, **param):
    reverse_flag = param.get('reverse')
    count = param.get('count', 0)

    with open(file_name) as fp:
        content = fp.readlines()

    if reverse_flag:
        content = content[::-1]

    if count:
        content = content[:count]

    return ''.join(content)

print cat('/etc/resolv.conf', reverse=True, count=1)