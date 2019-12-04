import timeit

def f_string_test():
    s = "World"
    return f"Hello, {s}!"

def percent_string_test():
    s = "World"
    return "Hello, %s!" %(s)

def string_arithmetic_test():
    s = "World"
    return "Hello, " + s + "!"

def format_string_test():
    s = "World"
    return "Hello, {}!".format(s)


num, rep = 1_000_000, 100
print(f'num, rep = {num:_}, {rep:_}\n')
print(f'string "+" string >> {min(timeit.repeat(string_arithmetic_test, number=num, repeat=rep)):0.4f}s')
print(f'string %s >> {min(timeit.repeat(percent_string_test, number=num, repeat=rep)):0.4f}s')
print(f'string.format >> {min(timeit.repeat(format_string_test, number=num, repeat=rep)):0.4f}s')
print(f'fstring >> {min(timeit.repeat(f_string_test, number=num, repeat=rep)):0.4f}s')

'''
num, rep = 1_000_000, 100

fstring >> 0.1333s
string "+" string >> 0.1606s
string %s >> 0.2458s
string.format >> 0.3012s

'''