import timeit

rang = 100_000

def test_list():
    return list(range(rang))

def test_comperhansion():
    return [x for x in range(rang)]


def list_making_test():

    num, rep = 1_000, 1
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}')
    print(f'list(range(number)) >> {min(timeit.repeat(test_list, number=num, repeat=rep)):0.4f}s')
    print(f'[x for x in range(number)] >> {min(timeit.repeat(test_comperhansion, number=num, repeat=rep)):0.4f}s')

list_making_test()
'''
num, rep = 1_000, 1
rang = 100_000

list(range(number)) >> 2.4979s
[x for x in range(number)] >> 3.6804s
'''