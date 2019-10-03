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

def a():
    return list(range(100_000))
print(min(timeit.repeat(a, number=1000, repeat=1)))

def b():
    return [x for x in range(100_000)]
print(min(timeit.repeat(b, number=1000, repeat=1)))