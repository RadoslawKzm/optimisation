import bisect
import timeit

lst1 = list(range(10_000_000))
for i in range(660_001, 660_010):
    lst1.pop(i)

lst2 = list(lst1)

def test_bisect():
    for i in range(660_001, 660_010):
        bisect.insort(lst1, i)
    return lst1

def test_sort():
    for i in range(660_001, 660_010):
        lst2.append(i)
    lst2.sort()
    return lst2


num, rep = 10, 10
print(f'num, rep = {num:_}, {rep:_}')
print(f'bisect >> {min(timeit.repeat(test_bisect, number=num, repeat=rep)):0.4f}s')
print(f'sort >> {min(timeit.repeat(test_sort, number=num, repeat=rep)):0.4f}s')

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




