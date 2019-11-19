from collections import deque
import timeit
from time import time

rang = 100_000_000
tstart = time()
lst = ['test' for _ in range(rang)]
print(f'done making list in {time()-tstart:0.4f}')

tstart = time()
deq = deque(['test' for _ in range(rang)])
print(f'done making deque in {time()-tstart:0.4f}')


def list_test():
    for _ in range(rang):
        lst.pop()

def deque_test():
    for _ in range(rang):
        deq.pop()

def test_suite():
    num, rep = 1, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'list_test >> {min(timeit.repeat(list_test, number=num, repeat=rep)):0.4f}s')
    print(f'deque_test >> {min(timeit.repeat(deque_test, number=num, repeat=rep)):0.4f}s')

test_suite()

'''
range = 100_000_000, num, rep = 1, 1
list_test >> 9.3798s
deque_test >> 8.6057s
'''



