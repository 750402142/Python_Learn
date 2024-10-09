import random

count_number = int(input('要求的次数'))
int_number = 0
for i in range(count_number):
    x = random.randint(0,1)
    y = random.randint(0,1)
    if x*x + y*y <=1:
        int_number = int_number + 1
pi = (int_number/count_number)*4
print(pi)

