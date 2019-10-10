from collections import Counter
import timeit


def not_common_numbers_test():
    rang = 10_000_000
    lst1 = list(range(rang))
    lst2 = list(range(1_000_000))

    def counter_test():
        cnt1 = Counter(lst1)
        cnt2 = Counter(lst2)
        cnt3 = cnt1 - cnt2
        return list(cnt3.keys())

    def counter_subtract_test():
        cnt1 = Counter(lst1)
        cnt2 = Counter(lst2)
        cnt1.subtract(cnt2)
        return list(+cnt1)

    def set_diference_test():
        st1 = set(lst1)
        st2 = set(lst2)
        st3 = st1.difference(st2)
        return list(st3)

    def set_minus_test():
        st1 = set(lst1)
        st2 = set(lst2)
        st3 = st1 - st2
        return list(st3)

    def for_i_in_list_test():
        lst3 = []
        for item in lst1:
            if item not in lst2:
                lst3.append(item)
        return lst3

    num, rep = 1, 10
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}')
    print(f'counter_test >> {min(timeit.repeat(counter_test, number=num, repeat=rep)):0.4f}s')
    print(f'counter subtract test >> {min(timeit.repeat(counter_subtract_test, number=num, repeat=rep)):0.4f}s')
    print(f'set_diference_test >> {min(timeit.repeat(set_diference_test, number=num, repeat=rep)):0.4f}s')
    print(f'set_minus_test >> {min(timeit.repeat(set_minus_test, number=num, repeat=rep)):0.4f}s')
    # print(f'for_i_in_list_test >> {min(timeit.repeat(for_i_in_list_test, number=num, repeat=rep)):0.4f}s') # dont use it works for small data det

'''
lst1 = list(range(10_000_000))
lst2 = list(range(1_000_000))
num, rep = 1, 10

counter_test >> 5.0527s
counter subtract test >> 2.7646s
set_diference_test >> 0.8165s
set_minus_test >> 0.8166s
'''


def list_making_test():
    rang = 100_000

    def test_list():
        return list(range(rang))

    def test_comperhansion():
        return [x for x in range(rang)]

    num, rep = 1_000, 1
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}')
    print(f'list(range(number)) >> {min(timeit.repeat(test_list, number=num, repeat=rep)):0.4f}s')
    print(f'[x for x in range(number)] >> {min(timeit.repeat(test_comperhansion, number=num, repeat=rep)):0.4f}s')
'''
num, rep = 1_000, 1
rang = 100_000

list(range(number)) >> 2.4979s
[x for x in range(number)] >> 3.6804s
'''


def list_coping_test():
    rang = 10_000
    lst = list(range(rang))
    def test_colon():
        c = lst[:]
        return c

    def test_list():
        d = list(lst)
        return d

    import copy
    def test_copy():
        e = copy.copy(lst)
        return e

    num, rep = 100_000, 3
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}\n')
    print(f'list[:] >> {min(timeit.repeat(test_colon, number=num, repeat=rep)):0.4f}s')
    print(f'list(list) >> {min(timeit.repeat(test_list, number=num, repeat=rep)):0.4f}s')
    print(f'copy.copy(list) >> {min(timeit.repeat(test_copy, number=num, repeat=rep)):0.4f}s')

'''
num, rep = 100_000, 3
lst = list(range(10_000))

list[:] >> 2.0909s
list(list) >> 1.9255s
copy.copy(list) >> 2.1818s
'''