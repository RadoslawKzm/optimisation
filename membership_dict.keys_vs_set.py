import timeit
rang = 1_000_000

st = set(range(rang))
st.add('test')
dictio = dict(zip(range(rang),range(rang)))
dictio['test'] = 1

def set_membership_test():
    return 'test' in st

def dict_membership_test():
    return 'test' in dictio.keys()


def test_suite():
    num, rep = 10_000_000, 10
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'set_membership_test >> {min(timeit.repeat(set_membership_test, number=num, repeat=rep)):0.4f}s')
    print(f'dict_membership_test >> {min(timeit.repeat(dict_membership_test, number=num, repeat=rep)):0.4f}s')

test_suite()

'''
range = 1_000_000, num, rep = 1000000, 10
set_membership_test >> 0.1381s
dict_membership_test >> 0.2396s

range = 1_000_000, num, rep = 10000000, 10
set_membership_test >> 1.2056s
dict_membership_test >> 2.0818s
'''











