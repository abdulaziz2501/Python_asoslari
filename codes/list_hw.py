"""
#pythonda random

import random

random.seed(1)

def list():
    for i in range(10):
        print(random.randint(0,10), end=" ")

list()
"""

#p-27

"""
def number(n):
    count =0
    for i in range (1, int(n)):
        if n%i==0:
            count+=1
            if i==n//i:
                count-=1
    return count
numbers=[]
for num in range (1, 1000):
    if number(num)==9:
        numbers.append(num)
print(numbers)
"""

#p-28

"""
numbers = []
count=0
for num in range(1, 100):
    if '3' in str(num):
        numbers.append(num)
        count+=1

print(numbers)
print(count)
"""

#p-29
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(2, 100):
    if is_prime(num):
        num_str = str(num)
        if num_str == num_str[::-1]:
            print(num)
"""

#q-1
"""
lst = [1, 2, "Hello", True]
new_lst = []

for element in lst:
    new_lst.append(type(element).__name__)

print(new_lst)
"""


"""
# birinchi listddagi elementlarning nechtasi ikkinchi listda borligini topish
jewels=[1, 2, 3, 4, 5]
stones=[1, 2, 3, 4, 5, 6]
k=0
for i in jewels:
    if i in stones:
        k +=1
print(k)
"""

"""
#perfect issue
look=[2, 7, 13, 14, 15, 16, 17, 18, 19, 20]
target=9
opp=[]
for i in range(len(look)):
    for k in range (i+1, len(look)):
        if look[i]+look[k]==target:
            opp.append(i)
            opp.append(k)
            print(opp)
            exit(0)
"""

"""
#n sonini m-darajasini topish, 2 ni 10 darajasi = 1024
def look(num, ex, result):
    if ex==0:
        return
    else:
        print(result)
        look(num, ex-1, num*result)

n = int(input("enter N: "))
m = int(input("enter M: "))
look(n, m, n)
"""










































































