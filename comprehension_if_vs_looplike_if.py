from time import time



#===== TESTS ==============================================
def loop_test():
    return 1 if True else 0

def loop_test2():
    if True:
        return 1
    else:
        return 0

#===== TESTING ENVIROMENT ==============================================
def test_suite(rang):
    tstart = time()
    for i in range(rang):
        loop_test()
    print(f"looplike time >> {time() - tstart:0.4f}s")


    tstart = time()
    for i in range(rang):
        loop_test2()
    print(f"comprehension time >> {time() - tstart:0.4f}s")

def test2():
    for i in range(8):
        rang = 10 ** i
        print(f"range >> {rang:_}")
        test_suite(rang)
        print("\n\n")

test2()

"""
range >> 100_000
looplike time >> 0.0079s
comprehension time >> 0.0072s

range >> 1_000_000
looplike time >> 0.0803s
comprehension time >> 0.0715s

range >> 10_000_000
looplike time >> 0.7668s
comprehension time >> 0.7211s

"""
























#===== SETUP ==============================================
test_word = 'a'
string_size = 1_000_000
test_string = 'a'*string_size



#===== TESTING ENVIROMENT ==============================================
def test1():
    test_list = []
    tstart = time()
    print(f"string size >> {string_size:_}")
    for letter in test_string:
        if letter == 'a':
            test_list.append(letter)
    print(f"looplike time >> {time() - tstart:0.4f}s")

    tstart = time()
    test_list = [letter for letter in test_string if letter == 'a']
    print(f"comprehension time >> {time() - tstart:0.4f}s")

# test1()

"""
string size >> 1_000_000
looplike time >> 0.0770s
comprehension time >> 0.0378s

string size >> 10_000_000
looplike time >> 0.7336s
comprehension time >> 0.3501s

string size >> 100_000_000
looplike time >> 7.9533s
comprehension time >> 3.5281s
"""
