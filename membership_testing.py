from collections import Counter
import timeit



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

def not_common_numbers_test():
    num, rep = 1, 10
    print(f'range = {rang:_}, num, rep = {num:_}, {rep:_}')
    print(f'counter_test >> {min(timeit.repeat(counter_test, number=num, repeat=rep)):0.4f}s')
    print(f'counter subtract test >> {min(timeit.repeat(counter_subtract_test, number=num, repeat=rep)):0.4f}s')
    print(f'set_diference_test >> {min(timeit.repeat(set_diference_test, number=num, repeat=rep)):0.4f}s')
    print(f'set_minus_test >> {min(timeit.repeat(set_minus_test, number=num, repeat=rep)):0.4f}s')
    print(f'for_i_in_list_test >> {min(timeit.repeat(for_i_in_list_test, number=num, repeat=rep)):0.4f}s') # dont use it works for small data det


not_common_numbers_test()

'''
lst1 = list(range(10_000_000))
lst2 = list(range(1_000_000))
num, rep = 1, 10

counter_test >> 5.0527s
counter subtract test >> 2.7646s
set_diference_test >> 0.8165s
set_minus_test >> 0.8166s
'''

