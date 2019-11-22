import timeit

a, b, c = True, True, True


def multiple_equals_test():
    if a == b == c:
        return True

def multiple_ands():
    if a == b and a == c and b == c:
        return True


def test_suite():
    num, rep = 200_000, 100
    print(f'num, rep = {num:_}, {rep:_}')
    print(f'multiple_ands >> {min(timeit.repeat(multiple_ands, number=num, repeat=rep)):0.4f}s')
    print(f'multiple_equals_test >> {min(timeit.repeat(multiple_equals_test, number=num, repeat=rep)):0.4f}s')

test_suite()

'''
num, rep = 100_000, 10
multiple_ands >> 0.0183s
multiple_equals_test >> 0.0139s

num, rep = 100_000, 100
multiple_ands >> 0.0166s
multiple_equals_test >> 0.0119s

num, rep = 200_000, 100
multiple_ands >> 0.0319s
multiple_equals_test >> 0.0238s
'''