import os
os.system("cls")

"""
lst1 = []
lst2 = list()

print (lst1)
print (lst2)
print(type(lst1))
print(type(lst2))
"""

"""
lst1=[10, True, "salom", 3.14]
lst2=list((10, True, "salom", 3.14))

print (lst1)
print (lst2)
"""

"""
lst1=[1, 2, 3, 4, 5]
lst2=list((1, 2, 3, 4, 5, 6, 7, 8))

print (len(lst1))
print (len(lst2))
"""

"""
lst1=[1, 2, 3, "salom", True, 3.14, 4, 5, 6]
print (lst1[0])
print (lst1[1])
print (lst1[-1])
print (lst1[3:])
print (lst1[::-1])
"""

#lst1=[1, 2, 3, 4, 5]
#lst1[0]=10
#print(lst1)

#print(list("salom dunyo"))


#lst=[1, 2, 3, 5, "salom dunyo", 3.14]
#for i in range (len(lst)):
#    print(i)

#lst=[1, 2, 3, 5, "salom dunyo", 3.14]
#for i in range(len(lst)):
#    print(lst[i], type(lst[i]))

#lst=[1, 2, 3, 4, 5]
#for value in lst:
#    print(value)

#list = [1, 23, 3, 45]
#for i in range(len(list)):
#    list[i]=10
#print(list)

#list=[1, 2, 3, "salom", 4, 5]
#list.append('a')
#print(list)

#lst=list()
#for i in range(4):
#    son=int(input(f"{i+1} - enter element: "))
#    lst.append(son)
#print(lst)

#lst=[1, 2, 3, 4, 5]
#lst.clear()
#print(lst)

#lst=[1,2,3,4,5]
#cpy=lst
#print(lst)
#print(cpy)

#lst=[1,2,3,4,5]
#cpy=lst
#lst.append("hello guys")
#print(lst)
#print(cpy)

#lst=[1, 2, 3, "however", 3.14, True, 3, 4, 4, 4, 5, 4, 6, 4]
#x=lst.count(4)
#print(x)

#lst=[1, 2, 3, "however", 3.14, True, 3, 4, 4, 4, 5, 4, 6, 4]
#print(lst.count(4))

"""
a=[1, 2, 3]
b=[4, 5, 6]
print(a+b)
print([a, b])
print(*a)
print(a)
print(a*5)
print(a*len(b))
"""

"""
a=[1, 2, 3, 4]
b=[5, 6, 7, 8]
if a==b:
    print("teng")
else:
    print("teng emas")
"""


"""
#birinchi listni oxiriga ikkinchi listni qo'shadi

fruits=['apple', 'apricot', 'pear', 'banana', 'cherry']
cars=['Bugatti', 'Ferrari', 'Rolls-Royce', 'Lamborgini']
fruits.extend(cars)
print(fruits)
"""

#fruits=['apple', 'apricot', 'pear', 'banana', 'cherry']
#cars=['Bugatti', 'Ferrari', 'Rolls-Royce', 'Lamborgini']
#all=fruits+cars
#fruits[0]=10
#print(all)

#index methods(

#lst=[1, 4, 5, 6, 7, 8, 9]
#print (lst.index(4))

#lst=[12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
#print(lst[2:])
#print(lst[2:].index(1))

#pop methods

"""
lst=[4, 55, 64, 32, 16, 32]

deleted_elements=lst.pop(1)

print(lst)
print("deleted_elements: ", deleted_elements)
"""

"""
lst=[4, 55, 64, 32, 16, 32]

deleted_elements=lst.pop(-1)

print(lst)
print("deleted_elements: ", deleted_elements)
"""

#insert methods

#lst=["Ilyos", "Laziz", "Bobur", "Diyor"]
#lst.insert(1, "Men")
#print(lst)


#lst=["Ilyos", "Laziz", "Bobur", "Diyor"]
#lst.insert(1, ["Men", "Elboy", "Samariddin"])
#print(lst)

#sort methods

#lst=[5, 2, 8, 5, 9, 0, 2, 1, 3, 6, 7]
#lst.sort()
#print(lst)


"""
# Piramida o'yini
son = int(input('Yulduzchali piramidaning qatorini kiriting:  '))
q = "0"
i = q + q
qator = 0
while True:
  if son > 0:
    for n in range(son):
      print(q.center(50))
      q += i
      qator += 1
  if qator == son:
    break
"""


#lst=[5, 2, 8, 5, 9, 0, 2, 1, 3, 6, 7]
#lst.sort(reverse=True)
#print(lst)

#lst=["Ilyos", "Laziz", "Bobur", "Diyor"]
#lst.sort()
#print(lst)

#reverse() methods -> bu faqat listni teskari tartibda chiqaradi

#lst=[8, 3, 2, 5, 8, 6, 9, 1, 4, 2]
#lst.reverse()
#print(lst)

#remove methods -> tanlangan elementni olib tashlaydi

#lst=[4, 1, 3, 2, 5, 7, 6, 8, 0, 9]
#lst.remove(3)
#print(lst)

#Ichma-ich for

#for i in range(10):
#    print("i =", i)
#    for k in range(5):
#        print("\tk =", k)


#for i in range(10):
#    print("i =", i)
#    for k in range(i+1):
#        print("\tk =", k)


#for i in range(1, 10):
#    print("i =", i)
#    for k in range(1, i+1):
#        print("\tk =", k)


"""
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(lst)):
    print(lst[i])
"""

"""
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in lst:
    print(i)
"""

"""
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(lst)):
    for k in range (len(lst[i])):
        print(lst[i][k], end=" ")
    print()
"""

"""
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in lst:
    for k in i:
        print(k, end=" ")
    print()
"""

#dioganal elementlarni '*' ga alishtirsh
"""
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if i==k or i+k==len(lst)-1:
            print("*", end=" ")
        else:
            print(lst[i][k], end=" ")
    print()
"""




































