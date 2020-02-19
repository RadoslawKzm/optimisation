import timeit

rang = 1_000_000
lst = [-1.5 for i in range(rang)]

def string_minus_test():
    result_list = []
    for item in lst:
        strin = str(item)
        if '-' in strin:
            result_list.append(strin[1:])

def less_than_test():
    result_list = []
    for item in lst:
        if item < 0:
            result_list.append(item)


def test_suite():
    num, rep = 1, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'string_minus_test >> {min(timeit.repeat(string_minus_test, number=num, repeat=rep)):0.4f}s')
    print(f'less_than_test >> {min(timeit.repeat(less_than_test, number=num, repeat=rep)):0.4f}s')

test_suite()

'''
range = 1_000_000, num, rep = 1, 1
string_minus_test >> 1.3014s
less_than_test >> 0.1286s
'''