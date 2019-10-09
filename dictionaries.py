import timeit


def senior_dev():
    return dict(enumerate(range(10_000)))

def medium_dev():
    return {p: v for p, v in enumerate(range(10_000))}

def junior_dev():
    dictio = {}
    for k, v in enumerate(range(10_000)):
        dictio[k] = v
    return dictio

num, rep = 1_000, 3
print('senior_dev >> ', min(timeit.repeat(senior_dev, number=num, repeat=rep)))
print('medium_dev >> ', min(timeit.repeat(medium_dev, number=num, repeat=rep)))
print('junior_dev >> ', min(timeit.repeat(junior_dev, number=num, repeat=rep)))



'''
num, rep = 1_000, 3

senior_dev >>  0.6572029499802738
medium_dev >>  0.7706875120056793
junior_dev >>  0.8078349230345339
'''

