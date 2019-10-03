
def a():
    s = "World"
    return "Hello, " + s + "!"
print(min(timeit.repeat(a, number=100_000, repeat=100)))

def b():
    s = "World"
    return f"Hello, {s}!"
print(min(timeit.repeat(b, number=100_000, repeat=100)))