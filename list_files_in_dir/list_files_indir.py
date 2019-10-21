#
# for item in ['ac', 'tr', 'sp']:
#     for i in range(10_000):
#         with open(f'test.{item}{i}', 'w'):
#             pass


import timeit
import glob
import os

def timing_test():
    def glob_test():
        st1 = {x for x in glob.glob('*')}
        return st1
    def walk_test():
        st1 = {x for _,_,y in os.walk('.') for x in y }
        return st1
    def listdir_test():
        st1 = {x for x in os.listdir()}
        return st1
    def scandir_test():
        st1 = {x.name for x in os.scandir() if x.is_file()}
        return st1
    def scandir_noif_test():
        st1 = {x.name for x in os.scandir()}
        return st1
    def scandir_noname_test():
        st1 = [x for x in os.scandir()]
        return st1


    num, rep = 100, 5
    print(f'num, rep = {num}, {rep}')
    print(f'glob_test >> {min(timeit.repeat(glob_test, number=num, repeat=rep)):0.4f}s')
    print(f'walk_test >> {min(timeit.repeat(walk_test, number=num, repeat=rep)):0.4f}s')
    print(f'listdir_test >> {min(timeit.repeat(listdir_test, number=num, repeat=rep)):0.4f}s')
    print(f'scandir_test >> {min(timeit.repeat(scandir_test, number=num, repeat=rep)):0.4f}s')
    print(f'scandir_noif_test >> {min(timeit.repeat(scandir_noif_test, number=num, repeat=rep)):0.4f}s')
    print(f'scandir_noname_test >> {min(timeit.repeat(scandir_noname_test, number=num, repeat=rep)):0.4f}s')

timing_test()

'''
#10_000 files x3 .extension in dir to list
num, rep = 1, 5
glob_test >> 0.0317s
walk_test >> 0.0338s
listdir_test >> 0.0093s
scandir_test >> 0.0294s
scandir_noif_test >> 0.0137s
scandir_noname_test >> 0.0122s

num, rep = 10, 5
glob_test >> 0.3431s
walk_test >> 0.3142s
listdir_test >> 0.0927s
scandir_test >> 0.2674s
scandir_noif_test >> 0.1299s
scandir_noname_test >> 0.1179s

num, rep = 100, 5
glob_test >> 3.1096s
walk_test >> 2.9234s
listdir_test >> 0.9354s
scandir_test >> 2.2523s
scandir_noif_test >> 1.3049s
scandir_noname_test >> 1.1627s
'''

'''
#100 files x3 .extension in dir to list 
num, rep = 1_000, 5
glob_test >> 0.3192s
walk_test >> 0.1990s
listdir_test >> 0.0780s
scandir_test >> 0.1425s
scandir_noif_test >> 0.1155s
scandir_noname_test >> 0.0875s

num, rep = 10_000, 5
glob_test >> 3.1858s
walk_test >> 1.9883s
listdir_test >> 0.7854s
scandir_test >> 1.4348s
scandir_noif_test >> 1.0515s
scandir_noname_test >> 0.9020s

num, rep = 100_000, 5
glob_test >> 29.7141s
walk_test >> 18.3203s
listdir_test >> 7.1681s
scandir_test >> 13.1344s
scandir_noif_test >> 10.5470s
scandir_noname_test >> 8.7443s
'''

