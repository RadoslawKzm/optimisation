import timeit


def timing_test():
    rang = 1_000_000
    lst = list(range(rang))

    def enumerate_test():
        return [k+v for k, v in enumerate(lst)]

    def len_test():
        return [lst[i]+i for i in range(len(lst))]

    num, rep = 10, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'enumerate_test >> {min(timeit.repeat(enumerate_test, number=num, repeat=rep)):0.4f}s')
    print(f'len_test >> {min(timeit.repeat(len_test, number=num, repeat=rep)):0.4f}s')

timing_test()

'''
range = 1_000_000, num, rep = 10, 1
enumerate_test >> 3.3295s
len_test >> 3.7283s
'''