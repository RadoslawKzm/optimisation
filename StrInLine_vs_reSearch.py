#!/depot/Python-3.6.2/bin/python

import re
import timeit

rang = 100_000_000
# with open('test', 'w') as file:
#     for i in range(rang):
#         file.write(f'TEST string must be quite long for good measurement when given big number of letters. Well Well Well lets see, how this test withh do with such long string to find in hehehehe :D. Jak do tego doszlo nie wiem :( i nasza testowa malpa @\n')
#         file.flush()


def re_search_test():
    with open('test') as file:
        for line in file:
            if re.search('@', line):
                pass

def re_search_local_imports_test():
    research = re.search
    with open('test') as file:
        for line in file:
            if research('@', line):
                pass

def re_search_compiled_test():
    pattern = re.compile('@')
    with open('test') as file:
        for line in file:
            if re.search(pattern, line):
                pass

def re_search_compiled_local_imports_test():
    recompile = re.compile
    research = re.search
    pattern = recompile('@')
    with open('test') as file:
        for line in file:
            if research(pattern, line):
                pass

def re_findall_test():
    with open('test') as file:
        for line in file:
            findall = re.findall('@', line)
            if findall:
                pass

def re_findall_local_imports_test():
    refindall = re.findall
    with open('test') as file:
        for line in file:
            findall = refindall('@', line)
            if findall:
                pass


def re_findall_compiled_test():
    pattern = re.compile('@')
    with open('test') as file:
        for line in file:
            findall = re.findall(pattern, line)
            if findall:
                pass

def re_findall_compiled_local_imports_test():
    pattern = re.compile('@')
    refindall = re.findall
    with open('test') as file:
        for line in file:
            findall = refindall(pattern, line)
            if findall:
                pass



def is_in_line_test():
    with open('test') as file:
        for line in file:
            if '@' in line:
                pass


def test_suite():
    num, rep = 1, 1
    print(f'lines in file= {rang:_}, num = {num:_}, rep = {rep:_}')
    print(f're_search_test >> {min(timeit.repeat(re_search_test, number=num, repeat=rep)):0.4f}s')
    print(f're_search_local_imports_test >> {min(timeit.repeat(re_search_local_imports_test, number=num, repeat=rep)):0.4f}s')
    print(f're_search_compiled_test >> {min(timeit.repeat(re_search_compiled_test, number=num, repeat=rep)):0.4f}s')
    print(f're_search_compiled_local_imports_test >> {min(timeit.repeat(re_search_compiled_local_imports_test, number=num, repeat=rep)):0.4f}s')
    print(f're_findall_test >> {min(timeit.repeat(re_findall_test, number=num, repeat=rep)):0.4f}s')
    print(f're_findall_local_imports_test >> {min(timeit.repeat(re_findall_local_imports_test, number=num, repeat=rep)):0.4f}s')
    print(f're_findall_compiled_test >> {min(timeit.repeat(re_findall_compiled_test, number=num, repeat=rep)):0.4f}s')
    print(f're_findall_compiled_local_imports_test >> {min(timeit.repeat(re_findall_compiled_local_imports_test, number=num, repeat=rep)):0.4f}s')
    print(f'is_in_line_test >> {min(timeit.repeat(is_in_line_test, number=num, repeat=rep)):0.4f}s')


test_suite()

# result = list_test()
'''
lines in file= 1_000_000, num = 1, rep = 1, ||| FILE_SIZE =225MB
re_search_test >> 1.0228s
re_search_local_imports_test >> 0.9968s
re_search_compiled_test >> 1.3872s
re_search_compiled_local_imports_test >> 1.3730s
re_findall_test >> 1.0310s
re_findall_local_imports_test >> 0.9880s
re_findall_compiled_test >> 1.3849s
re_findall_compiled_local_imports_test >> 1.3700s
is_in_line_test >> 0.2402s

lines in file= 100_000_000, num = 1, rep = 1 ||| FILE_SIZE =22.5GB
re_search_test >> 107.6511s
re_search_local_imports_test >> 104.8313s
re_search_compiled_test >> 144.4875s
re_search_compiled_local_imports_test >> 139.2302s
re_findall_test >> 112.2644s
re_findall_local_imports_test >> 109.3807s
re_findall_compiled_test >> 151.9309s
re_findall_compiled_local_imports_test >> 144.6272s
is_in_line_test >> 31.9664s
'''

"""conclusion: DO NOT USE REGEX if you dont need to, I think there's no need to explain why rly"""