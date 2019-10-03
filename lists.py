from collections import Counter
import time
import timeit

# tstart = time.time()
# lst1 = list(range(10_000_000))
# lst2 = list(range(1_000_000))
# cnt1 = Counter(lst1)
# cnt2 = Counter(lst2)
# cnt3 = cnt1 - cnt2
# lst3 = list(cnt3.keys())
# tend = time.time()
# #
# print(tend-tstart)

# tstart = time.time()
# lst1 = list(range(10_000_000))
# lst2 = list(range(1_000_000))
# st1 = set(lst1)
# st2 = set(lst2)
# st3 = st1.difference(st2)
# lst3 = list(st3)
# tend = time.time()
#
# print(tend-tstart)
#
# tstart = time.time()
# lst1 = list(range(10_000_000))
# lst2 = list(range(1_000_000))
# st1 = set(lst1)
# st2 = set(lst2)
# st3 = st1 - st2
# lst3 = list(st3)
# tend = time.time()

# lst =[]
# for i in range(10):
#     lst.append(i)
#     lst.append(i+0.5)
# print(lst)
from dis import dis

def a():
    return list(range(100_000))
# print(min(timeit.repeat(a, number=1000, repeat=1)))

def b():
    return [x for x in range(100_000)]
# print(min(timeit.repeat(b, number=1000, repeat=1)))


num, rep = 100_000, 3
lst = list(range(10_000))
def c():
    c = lst[:]
    return c
print(min(timeit.repeat(c, number=num, repeat=rep)))

def d():
    d = list(lst)
    return d
print(min(timeit.repeat(d, number=num, repeat=rep)))

import copy
def e():
    e = copy.copy(lst)
    return e
print(min(timeit.repeat(e, number=num, repeat=rep)))

