import timeit

'''Checking if for is faster than while loop,
genesis is Learning python states that for loop is writen mainly in c and while is writen mainly in python,
thus for should be faster than while
'''

def for_test():
    file = open('test_file')
    for line in file:
        if 'radek' in line:
            break
    file.close()

def while_test():
    file = open('test_file')
    line = file.readline()
    while line != 'radek':
        line = file.readline()
    file.close()

num, rep = 1, 10
print(f'num, rep = {num}, {rep}')
print(f'for_test >> {min(timeit.repeat(for_test, number=num, repeat=rep)):0.4f}s')
print(f'while_test >> {min(timeit.repeat(while_test, number=num, repeat=rep)):0.4f}s')

'''
num, rep = 1, 1
for_test >> 4.8775s
while_test >> 4.8980s

num, rep = 5, 1
for_test >> 24.0330s
while_test >> 24.0097s

num, rep = 1, 5
for_test >> 4.3572s
while_test >> 5.0191s

num, rep = 1, 10
for_test >> 6.5127s
while_test >> 6.8234s

so while loop we can say is equal to for loop instead of book wisdom. 
Lesson learned don't belive in books  relentlessly, they aren't always right
Always check stuff you are told, it prolongs learning but what you get is polished and refined knowlage and 
    mostly correct knowlage. 
'''





# test_file = open('test_file', 'w')
# for i in range(10_000_000):
#     test_file.write("let's see this is testing line in for vs while loop confrontation\n")
# test_file.write('radek')
# test_file.close()
#test string appended 'radek'


