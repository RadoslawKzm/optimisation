import timeit
from operator import itemgetter, attrgetter

def lambda_itmgtr_test():
    rang = 1_000_000
    student_tuples = [('john', 'a', x) for x in reversed(range(rang))]
    def lambda_test():
        return sorted(student_tuples, key=lambda student: student[2])


    def itemgetter_test():
        return sorted(student_tuples, key=itemgetter(2))

    num, rep = 100, 1
    print(f'range = {rang:_}, num, rep = {num}, {rep}')
    print(f'lambda >> {min(timeit.repeat(lambda_test, number=num, repeat=rep)):0.4f}s')
    print(f'itemgetter >> {min(timeit.repeat(itemgetter_test, number=num, repeat=rep)):0.4f}s')

lambda_itmgtr_test()

'''
range = 1_000_000, num, rep = 100, 1
lambda >> 10.9417s
itemgetter >> 8.1245s

'''