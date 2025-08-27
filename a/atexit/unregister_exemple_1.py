def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
print('66666666666')

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')

atexit.unregister(goodbye)


"""
66666666666
Goodbye Donny, it was nice to meet you.
"""