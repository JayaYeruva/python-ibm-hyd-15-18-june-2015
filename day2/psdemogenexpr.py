__author__ = 'ravi'

def grep_me(file_name, selection):
    return (line.rstrip()
            for line in open(file_name) if line.startswith(selection))

path = r'c:\blah\file1'

g = grep_me('/etc/passwd', 'a')
print g.next()

#for i in g:
#   print i
