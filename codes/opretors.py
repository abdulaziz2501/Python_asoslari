import os
os.system("cls")

#print ("%.1f" % (20.345))

"""
x=5
y=10
z=22
print(max(x,y,z))
print(min(x,y,z))
"""

#x, y, z = "London", True, 22
#print (x, y, z)

#   && -> and
#   // -> or
#   ! -> not

"""
num1=-30
num2=20

if num1>num2:
    print (num1)
else:
    print (num2)
"""
"""
son = 22
if son>0:
    print ("Musbat")
else:
    if son<0:
        print ("Manfiy")
    else:
        print ("nolga teng")
"""

"""
son = int(input("sonni kiriting:"))

if son>0:
    print ("Musbat")
elif son<0:
    print ("Manfiy")
else:
    print ("nolga teng")
"""

"""
num1 = int(input("num1 kiriting: "))
num2 = int(input("num2 kiriting: "))
num3 = int(input("num3 kiriting: "))

if num1>num2 and num1<num3 or num1>num3 and num1<num2:
    print(num1)
elif num2>num3 and num2<num1 or num2>num1 and num2<num3:
    print(num2)
elif num3>num1 and num3<num2 or num3>num2 and num3<num1:
    print(num3)
else:
    print("sonlar teng")
"""

"""
print (True or False)
print (True and False)

print ("Alone" or 123)
print ("Alone" and 123)
"""

#print (not True)
#print (not "Alone")

"""
surname = input ()
if surname =="":
    surname = "Player"
print (surname)
"""

#surname = input () or "Player"
#print (surname)

"""
word = "Salom, Ali bankka telefon qil. Ipoteka bankiga"

if not(word.find("bank") == -1):
    print ("bor")
else:
    print ("yo'q")
"""

"""
word = "Salom, Ali bankka telefon qil. Ipoteka bankiga"
search=input("search: ")

if word.find(search) != -1:
    print ("bor")
else:
    print ("yo'q")
"""

"""
word = "Salom, Ali bankka telefon qil. Ipoteka bankiga"
search=input("search: ")

if word.lower().find(search.lower()) != -1:
    print ("bor")
else:
    print ("yo'q")
"""

#word = "Salom, Ali bankka telefon qil. Ipoteka bankiga"
#search = input ("search: ")
#print (search in word)

#word = "good morning"
#search = input ("search: ")
#print (search not in word)


"""
word = "good morning"
search = input ("search: ")

if search in word:
    print ("bor")
else:
    print ("yo'q")
"""

#start = 1
#while start<=10:
#    print(start)
#    start +=1

"""
start = 1
stop = int(input ("stop: "))
while start <= stop:
    print(start)
    start +=1
"""

"""
start = 1
stop = int(input("stop: "))
while start<=stop:
    print(stop)
    stop  -=1
"""

"""
start = 1
stop = int(input("stop: "))
while start<=stop:
    if stop%2==0:
        print(stop)
    stop  -=1
"""

"""
start = 1
stop = int(input("stop: "))
while start<=stop:
    if not stop%2:
        print(stop)
    stop  -=1
"""

"""
#find prime number

num = int(input("Enter num: "))
i=2
check = True

while i<= num ** (1/2):
    if not num % i:
        check = False
        break
    i+=1
if check:
    print ("num is prime")
else:
    print ("num is not prime")


num = int(input("Enter num = "))
i=2
check = True

while i<= num **(1/2):
    if not num % i:
        check = False
        break
    i+=1
print ("Num is prime" if check else "Num is not prime")
"""

#print (list(range(10)))
#print (list(range(10, 20)))
#print (list(range(10, 30, 2)))

#print (list(range(-10, 0, +1)))

#for i in range (10):
#    print (i)

#for i in range (10):
#    print(i+10)

#for i in range (10):
#    if not i%2:
#        print (i)

#for i in range (40, 20, -1):
#    if not i%2:
#        print (i)


#for i in range (1, 20, 2):
#    print (i)


#st = "My name is Mukhtor"
#for i in range (len(st)):
#    print (st[i], end="")


#st = "My name is Mukhtor"
#for i in range (len(st)):
#    if st[i].isupper():
#        print (st[i], end="")


#st = "My name is Mukhtor"
#for i in st:
#    print(i, end="")


#print (ord("a"))
#print (chr(102))
#print (chr(ord('a')+2))































































