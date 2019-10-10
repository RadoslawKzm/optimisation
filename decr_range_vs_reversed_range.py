import timeit

def range_reversed_test():
    rang = 100_000

    def range_test():
        return [('john', 'a', x) for x in range(rang, 0, -1)]


    def reversed_test():
        return [('john', 'a', x) for x in reversed(range(rang))]


    num, rep = 100, 5
    print('range(::-1)>> ', min(timeit.repeat(range_test, number=num, repeat=rep)))
    print('reversed(range) >> ', min(timeit.repeat(reversed_test, number=num, repeat=rep)))

# range_reversed_test()

'''
rang = 100_000_000, num, rep = 1, 1
range(::-1)>>  10.805012283999531
reversed(range) >>  10.053456900997844

rang = 100_000, num, rep = 100, 5
range(::-1)>>  0.9705780479998793
reversed(range) >>  0.969862837002438

'''

def disasemble_test():
    from dis import dis
    rang = 10

    def range_test():
        return [('john', 'a', x) for x in range(rang, 0, -1)]


    def reversed_test():
        return [('john', 'a', x) for x in reversed(range(rang))]

    dis(range_test)
    txt = 'placeholder'
    print(f'\n {txt:=^101}\n')
    dis(reversed_test)

# disasemble_test()