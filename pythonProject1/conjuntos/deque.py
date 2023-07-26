"""
Modulo Collections - Deque
Documentation: https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance

"""

from collections import deque

deq = deque('robert')

print(deq)

d = deque('moraes')

deq.append('m')
deq.append('o')
deq.append('r')
deq.append('a')
deq.append('e')
deq.append('s')


print(deq)
