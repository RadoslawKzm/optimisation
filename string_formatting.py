import timeit
def string_arithmetic_test():
    s = "World"
    return "Hello, " + s + "!"

def format_string_test():
    s = "World"
    return "Hello, {}!".format(s)

def f_string_test():
    s = "World"
    return f"Hello, {s}!"

num, rep = 1_000_000, 100
print('string "+" string >> ', min(timeit.repeat(string_arithmetic_test, number=num, repeat=rep)))
print('string.format >> ', min(timeit.repeat(format_string_test, number=num, repeat=rep)))
print('fstring >> ', min(timeit.repeat(f_string_test, number=num, repeat=rep)))

'''
num, rep = 1_000_000, 100

string "+" string >>  0.1584004471078515
string.format >>  0.2886155489832163
fstring >>  0.13300530705600977
'''