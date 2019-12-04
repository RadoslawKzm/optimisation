import timeit
rang = 1_000_000



def zip_test():
    return dict(zip(range(rang), range(rang)))

def enumerate_test():
    return dict(enumerate(range(rang)))


def test_suite():
    num, rep = 1, 100
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'zip_test >> {min(timeit.repeat(zip_test, number=num, repeat=rep)):0.4f}s')
    print(f'enumerate_test >> {min(timeit.repeat(enumerate_test, number=num, repeat=rep)):0.4f}s')

test_suite()

'''
range = 1_000_000, num, rep = 1, 10
zip_test >> 0.1746s
enumerate_test >> 0.1789s

range = 1_000_000, num, rep = 1, 100
zip_test >> 0.1163s
enumerate_test >> 0.1165s
'''