from time import time


#===== SETUP ==============================================
test_word = 'test'
string_size = 10_000_000
test_string = test_word + ' some'*string_size


#===== TESTS ==============================================
def startswith_test(runs: int):
    if test_string.startswith(test_word):
        pass

def word_in_line_test(runs: int):
    if test_word in test_string:
        pass


#===== TESTING ENVIROMENT ==============================================
def testing_suite2(parallel_runs: int, series_runs: int):
    tests = [startswith_test, word_in_line_test]
    results = {"startswith": 0, "word_in": 0}

    for run in range(parallel_runs):
        for test in tests:
            for series_run in range(series_runs):
                tstart = time()
                test = test_string.startswith(test_word)
                tend = time() - tstart
                results["startswith"] += tend

                tstart = time()
                test = test_word in test_string
                tend = time() - tstart
                results["word_in"] += tend

    print(f"number of parallel_runs >> {parallel_runs:_}")
    print(f"number of series_runs >> {series_runs:_}")
    print(f"startswith elapsed mean time = {results['startswith'] / parallel_runs:0.4f}s")
    print(f"startswith elapsed summaric time = {results['startswith']:0.4f}s")

    print(f"word_in elapsed mean time = {results['word_in'] / parallel_runs:0.4f}s")
    print(f"word_in elapsed summaric time = {results['word_in']:0.4f}s")


testing_suite2(parallel_runs=1_000_000, series_runs=1)

"""
number of parallel_runs >> 1
number of series_runs >> 1_000_000
startswith elapsed mean time = 0.4990s
startswith elapsed summaric time = 0.4990s
word_in elapsed mean time = 0.2695s
word_in elapsed summaric time = 0.2695s

number of parallel_runs >> 1_000_000
number of series_runs >> 1
startswith elapsed summaric time = 0.4836s
word_in elapsed summaric time = 0.2544s
"""


























# legacy code b4 realisation that def is slowing down performance and each def call costs time
#
#
#
#
#
#
# #===== TESTING ENVIROMENT ==============================================
# def testing_suite(parallel_runs: int, series_runs: int):
#     results = {test.__name__: 0 for test in tests}
#
#     for run in range(parallel_runs):
#         for test in tests:
#             for series_run in range(series_runs):
#                 tstart = time()
#                 test(series_runs)
#                 tend = time() - tstart
#                 results[test.__name__] += tend
#
#     print(f"number of parallel_runs >> {parallel_runs:_}")
#     print(f"number of series_runs >> {series_runs:_}")
#     for test in tests:
#         print(f"{test.__name__} elapsed mean time = {results[test.__name__] / parallel_runs:0.4f}s")
#         print(f"{test.__name__} elapsed summaric time = {results[test.__name__]:0.4f}s")
#
#
# # testing_suite(parallel_runs=1_000_000, series_runs=100)