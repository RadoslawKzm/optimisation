from collections import deque
import timeit
from time import time

rang = 100_000_000

def list_test():
    lst = []
    for _ in range(rang):
        lst.append('test')
    return lst

def listcomp_test():
    lst = ['test' for _ in range(rang)]
    return lst

def deque_test():
    deq = deque()
    for _ in range(rang):
        deq.append('test')
    return deq

def deque2_test():
    deq = deque(['test' for _ in range(rang)])
    return deq


def test_suite():
    num, rep = 1, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'list_test >> {min(timeit.repeat(list_test, number=num, repeat=rep)):0.4f}s')
    print(f'listcomp_test >> {min(timeit.repeat(listcomp_test, number=num, repeat=rep)):0.4f}s')
    print(f'deque_test >> {min(timeit.repeat(deque_test, number=num, repeat=rep)):0.4f}s')
    print(f'deque2_test >> {min(timeit.repeat(deque2_test, number=num, repeat=rep)):0.4f}s')

test_suite()

# result = list_test()
'''
range = 10_000_000, num, rep = 1, 1
list_test >> 1.2893s
listcomp_test >> 0.7814s
deque_test >> 0.8038s
deque2_test >> 0.8721s

range = 100_000_000, num, rep = 1, 1
list_test >> 11.3185s
listcomp_test >> 7.5877s
deque_test >> 8.3456s
deque2_test >> 9.2025s
'''