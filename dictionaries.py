import timeit

# num, rep = 1_000, 3

# def a():
#     # l = range(50, -50, -2)
#     l = range(10_000)
#     d = {}
#     for p, v in enumerate(l):
#         d[p] = v
#     return d
# # print(min(timeit.repeat(a, number=num, repeat=rep)))
#
# def b():
#     # l = range(50, -50, -2)
#     l = range(10_000)
#     return {p: v for p, v in enumerate(l)}
# # print(min(timeit.repeat(b, number=num, repeat=rep)))

num, rep = 1_000, 3
def senior_dev():
    return dict(enumerate(range(10_000)))
print('senior_dev >> ', min(timeit.repeat(senior_dev, number=num, repeat=rep)))

def medium_dev():
    return {p: v for p, v in enumerate(range(10_000))}
print('medium_dev >> ', min(timeit.repeat(medium_dev, number=num, repeat=rep)))

def junior_dev():
    dictio = {}
    for k, v in enumerate(range(10_000)):
        dictio[k] = v
    return dictio
print('junior_dev >> ', min(timeit.repeat(junior_dev, number=num, repeat=rep)))





