from collections import deque
import timeit


def generator(rang:int):
    for i in range(rang):
        yield 'test'

rang = 100_000_000

def list_test():
    return list(generator(rang))

def deque_test():
    return deque(generator(rang))

def dict_test():
    return dict(zip(range(rang),generator(rang)))


def test_suite():
    num, rep = 1, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'list_test >> {min(timeit.repeat(list_test, number=num, repeat=rep)):0.4f}s')
    print(f'deque_test >> {min(timeit.repeat(deque_test, number=num, repeat=rep)):0.4f}s')
    print(f'dict_test >> {min(timeit.repeat(dict_test, number=num, repeat=rep)):0.4f}s')

# test_suite()

'''
range = 100_000_000, num, rep = 1, 1
list_test >> 12.1594s
deque_test >> 9.6937s
dict_test >> 20.2147s
'''


def list_test2():
    lst = []
    for item in range(rang):
        lst.append(item)
    return lst

def listcomp_test2():
    lst = [item for item in range(rang)]
    return lst

def deque_test2():
    deq = deque()
    for item in range(rang):
        deq.append(item)
    return deq

def dict_test2():
    dictio = {}
    for item in range(rang):
        dictio[item] = 1
    return dictio


def test_suite2():
    num, rep = 1, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'list_test2 >> {min(timeit.repeat(list_test2, number=num, repeat=rep)):0.4f}s')
    print(f'listcomp_test2 >> {min(timeit.repeat(listcomp_test2, number=num, repeat=rep)):0.4f}s')
    print(f'deque_test2 >> {min(timeit.repeat(deque_test2, number=num, repeat=rep)):0.4f}s')
    print(f'dict_test2 >> {min(timeit.repeat(dict_test2, number=num, repeat=rep)):0.4f}s')

test_suite2()

'''
range = 100_000_000, num, rep = 1, 1
list_test2 >> 27.5811s
deque_test2 >> 18.1669s
dict_test2 >> 82.6682s

range = 100_000_000, num, rep = 1, 1
list_test2 >> 19.2315s
listcomp_test2 >> 13.0801s
deque_test2 >> 10.2608s
dict_test2 >> 45.5202s
'''