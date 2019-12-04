import bisect
import timeit
from random import randint as random_randint


def prepare_lists(rang:int, random_numbers:set):
    lst1 = list(range(rang))
    for number in random_numbers:
        lst1.pop(lst1.index(number))
    return lst1

def bisect_test():
    for number in random_numbers:
        bisect.insort(lst, number)
    return lst

def bisect_test2():
    return [bisect.insort(lst, number) for number in random_numbers]

def sort_test():
    for number in random_numbers:
        lst.append(number)
    lst.sort()
    return lst


def test_suite(quantity_new_numbers:int=1):
    global lst
    global random_numbers
    number_pool = 10_000_000
    random_numbers = set()
    while len(random_numbers) != quantity_new_numbers:
        random_numbers.add(random_randint(0, number_pool))

    serial_runs, paralel_runs = 1, 50
    print(f'numbers changed >> {quantity_new_numbers}, serial runs = {serial_runs:_},  pararel runs = {paralel_runs:_}')
    lst = prepare_lists(number_pool, random_numbers)
    print(f'bisect_test >> {min(timeit.repeat(stmt=bisect_test, number=serial_runs, repeat=paralel_runs)):0.4f}s')
    lst = prepare_lists(number_pool, random_numbers)
    print(f'bisect_test2 >> {min(timeit.repeat(bisect_test2, number=serial_runs, repeat=paralel_runs)):0.4f}s')
    lst = prepare_lists(number_pool, random_numbers)
    print(f'sort_test >> {min(timeit.repeat(sort_test, number=serial_runs, repeat=paralel_runs)):0.4f}s')

test_suite(15)

'''
numbers changed >> 1, serial runs = 1,  paralel runs = 1
bisect_test >> 0.0084s
bisect_test2 >> 0.0078s
sort_test >> 0.1333s

numbers changed >> 1, serial runs = 1,  paralel runs = 50
bisect_test >> 0.0002s
bisect_test2 >> 0.0002s
sort_test >> 0.1758s

bisect_test >> 0.0562s
bisect_test2 >> 0.0725s
sort_test >> 0.1692s

numbers changed >> 15, serial runs = 1,  pararel runs = 50
bisect_test >> 0.1009s
bisect_test2 >> 0.0944s
sort_test >> 0.1166s

numbers changed >> 20, serial runs = 1,  pararel runs = 50
bisect_test >> 0.1405s
bisect_test2 >> 0.1759s
sort_test >> 0.1183s

numbers changed >> 100, serial runs = 1,  pararel runs = 50
bisect_test >> 0.5812s
bisect_test2 >> 0.6332s
sort_test >> 0.1185s

conclusion:
bisect is 15.5 times faster than sorting whole list but each iteration goes thru whole list to find position to insert
in the other hand sort shufles all list but does it only 1 time no matter of appended items
Use bisect if u have less than 15 items to add to whole list, if you have multiple big sets of data to add and sort to list append it and than sort
'''

















#legacy
'''
num10 rep10 run 1 append: 
bisect >>  0.07495053205639124
sort >>  1.0865776590071619

num10 rep10 run 10 append:
bisect >>  0.674495498999022
sort >>  1.0843172270106152

conclusion:
bisect is 15.5 times faster than sorting whole list but each iteration goes thru whole list to find position to insert
in the other hand sort shufles all list but does it only 1 time no matter of appended items
Use bisect if u have few items to add to whole list, if you have multiple big sets of data to add and sort to list append it and than sort
'''




