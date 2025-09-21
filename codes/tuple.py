from os import system
system ("cls")
"""
son=int(input("son kiriting: "))

for i in range (2, son + 1):
    count=0
    cpy=i
    for k in range (1, i+1):
        i=cpy
        while i>=k:
            i-=k
        if not i:
            count +=1

    if count ==2:
        print(cpy)
"""

"""
lst=[1, 2, 3, 4, 5]
tpl=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(lst)
print(tpl)
print(type(lst))
print(type(tpl))
"""

"""
lst=[1, 2, 3, 4, 5]
tpl=(1, 2, 3, "alone", 6, 7, True, 8, 9)
print(lst[3])
print(tpl[3])
"""

# tuple da qiymatlarni o'zgartirib bo'lmaydi

"""
lst=[1, 2, 3, 4, 5]
tpl=(1, 2, 3, "alone", 6, 7, True, 8, 9)
print (tpl)
print (tpl[3])
print (len(tpl))
print (type(tpl))
"""

"""
tpl=(1, 3, 4, 5, 6, "alone", True, 7, 8)
lst=tpl
print(tpl)
print(lst)
"""

"""
tpl=(1, 3, 4, 5, 6, "alone", True, 7, 8)
lst=list(tpl)
print(tpl)
print(lst)
"""

"""
tpl=(1, 2, 3, "alone", True, 4, 5, 6)
lst=list(tpl)
lst.append(7)
print(tpl)
print(lst)
"""

"""
# changes value of tuple

tpl=(1, 2, 3, "alone", True, 4, 5, 6)
lst=list(tpl)
lst.append(22)
tpl=tuple(lst)
print(tpl)
print(lst)
"""

"""
tpl=(1, 2, 3, "alone", True, 4, 5, 6)
tpl=list(tpl)
tpl.append("lonely")
print(tuple(tpl))
"""

#tpl=(1, 2, 3, "alone", True, 4, 5, 6, [7, 8, 9])
#tpl[-1].append(22)
#print(tpl)

#tpl=(1, 2, 3, "alone", True, 4, 5, 6, [7, 8, 9])
#print(tpl[3:])


"""
tpl=(1, 2, 3, "alone", True, 4, 5, 6, (7, 8, 9))
tpl=list((*list(tpl[:-1]), list(tpl[-1])))
tpl[-1].append(22)
tpl[-1]=tuple(tpl[-1])
tpl=tuple(tpl)
print(tpl)
"""

#tpl=(3.14,)
#print(tpl)
#print(type(tpl))


#tpl=(10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 10, 10)
#x=tpl.count(10)
#print(x)


#tpl=(10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 10, 10)
#x=tpl.index(50)
#print(tpl)
#print(x)

#tpl=(10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 10, 10)
#x=tpl.index(10, 2)
#print(x)

#tpl=(10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 10, 10)
#x=tpl.index(10, 5)
#print(x)



































































































