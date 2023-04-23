# Generator expression, Iterables e Iterators em Python 

import sys
iterable = ['Eu', 'Tenho', '_iter_']
iterator = iter(iterable) # tem _inter_ e _next_

"""
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

# aula90 2
lista= [n for n in range (1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))