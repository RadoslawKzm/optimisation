import timeit


def set_test():

    def set_braces():
        return {0,1,2,3,4,5,6,7,8,9}

    def set_range():
        return set(range(10))


    num, rep = 1_000_000, 1
    print(f'num, rep = {num}, {rep}')
    print(f'set braces >> {min(timeit.repeat(set_braces, number=num, repeat=rep)):0.4f}s')
    print(f'set range >> {min(timeit.repeat(set_range, number=num, repeat=rep)):0.4f}s')