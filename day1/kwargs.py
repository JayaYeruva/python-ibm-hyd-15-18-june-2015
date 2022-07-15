__author__ = 'ravi'


def demo(**param):
   print param
   print param.get('release')

demo()
demo(name='pypi', version=3.7, release='beffy cow')

info = {'release': 'beffy cow', 'pm': 'cpan','version': 3.7, 'name': 'pypi'}
demo(**info)

