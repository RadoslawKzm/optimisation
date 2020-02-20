from time import time


#===== SETUP ==============================================
test_word = 'test'
string_size = 10_000_000
test_string = test_word + ' some'*string_size



#===== TESTS ==============================================
def word_in_line_test():
    if test_word in test_string:
        pass


#===== TESTING ENVIROMENT ==============================================
for i in range(4, 8):
    rang = 10**i
    print(f"\n\nnumber of repeats >> {rang:_}")
    tstart = time()
    for i in range(rang):
        word_in_line_test()
    print(f"elapsed time def test >> {time() - tstart:0.4f}")

    tstart = time()
    for i in range(rang):
        if test_word in test_string:
            pass
    print(f"standalone time def test >> {time() - tstart:0.4f}")


"""
number of repeats >> 10_000
elapsed time def test >> 0.0013
standalone time def test >> 0.0006


number of repeats >> 100_000
elapsed time def test >> 0.0130
standalone time def test >> 0.0065


number of repeats >> 1_000_000
elapsed time def test >> 0.1302
standalone time def test >> 0.0648


number of repeats >> 10_000_000
elapsed time def test >> 1.3002
standalone time def test >> 0.6565


number of repeats >> 100_000_000
elapsed time def test >> 13.0606
standalone time def test >> 6.4827

visible linearity
"""