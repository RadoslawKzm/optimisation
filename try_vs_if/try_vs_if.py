import timeit
import matplotlib
import numpy as np
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def letter_gen(rang:int):
    for i in range(rang):
        yield 'a'

def float_gen(start, stop, step):
    for number in np.arange(start=start, stop=stop, step=step):
        yield number


def try_test():
    for i in range(rang_true):
        try:
            a = i/1
        except TypeError:
            pass
    for letter in letter_gen(rang_false):
        try:
            a = letter/1
        except TypeError:
            pass

def if_test():
    for i in range(rang_true):
        if isinstance(i, int):
            a = i/1
        else:
            pass
    for letter in letter_gen(rang_false):
        if isinstance(letter, int):
            a = letter/1
        else:
            pass


def test_suite():
    num, rep = 1, 1
    try_test_result = min(timeit.repeat(try_test, number=num, repeat=rep))
    if_test_result = min(timeit.repeat(if_test, number=num, repeat=rep))
    return try_test_result, if_test_result

def looping_func(start, end, step):
    global rang_true
    global rang_false
    results_try = {}
    results_if = {}
    for i in float_gen(start, end, step):
        print(f'percent processing >> {i:0.4f}%')
        percent = i  # percent of true occrances
        rang_true = 1_000_000
        rang_false = int(rang_true * (100 / percent) - rang_true)
        results = test_suite()
        results_try[i] = results[0]
        results_if[i] = results[1]
    return results_try, results_if


start, stop, step = 80, 100, 0.1
stop = stop+step

dictio = looping_func(start,stop,step)
try_results = dictio[0]
if_results = dictio[1]


plt.plot(tuple(try_results.keys()), tuple(try_results.values()), label='try_test')
plt.plot(tuple(if_results.keys()), tuple(if_results.values()), label='if_test')
plt.title(f'range>>{rang_true+rang_false:_}')
plt.xlabel('positive result of if/try [%]')
plt.ylabel('time of execusion [s]')
plt.legend()




'''
try looses with if till about 82% of true/error ratio, after 82% try is getting significant advantages
'''