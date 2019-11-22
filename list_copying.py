import timeit
import copy

rang = 10_000
lst = list(range(rang))


def test_colon():
    c = lst[:]
    return c

def test_list():
    d = list(lst)
    return d

def test_copy():
    e = copy.copy(lst)
    return e

def list_copying_test():
    num, rep = 100_000, 3
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}\n')
    print(f'list[:] >> {min(timeit.repeat(test_colon, number=num, repeat=rep)):0.4f}s')
    print(f'list(list) >> {min(timeit.repeat(test_list, number=num, repeat=rep)):0.4f}s')
    print(f'copy.copy(list) >> {min(timeit.repeat(test_copy, number=num, repeat=rep)):0.4f}s')

list_copying_test()
'''
num, rep = 100_000, 3
lst = list(range(10_000))

list[:] >> 2.0909s
list(list) >> 1.9255s
copy.copy(list) >> 2.1818s
'''