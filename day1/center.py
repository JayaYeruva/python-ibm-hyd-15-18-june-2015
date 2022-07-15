__author__ = 'ravi'


def center(string_content, width, fill=' '):
    n_times = (width - len(string_content)) / 2
    return "{}{}{}".format(fill * n_times, string_content, fill * n_times)

print center('perl', 8, '-')
print 'perl'.center(8, '-')



