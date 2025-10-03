# data structure :

# list - ro'yxat
# tuple - kortej
# set - toplam
# dictionary - lug'at

# a=[]- qiymati yoq list
# a=[] - list ga ma'lumot qo'shib bo'ladi
# b=() - tuple o'zgarmas 
# c={} - set unique qiymat qoldiradi


# print(b.index("ism")) - indexini qaytaradi
# print(b.count(45)) - element necha martta ishtirok etganini sanaydi

# b=(45, "ism", True, 45)

 # setga ma'lumot qo'shadi
# c.clear() -  butunlay hammasini o'chirad

# c={12, 43, 54, 12, 43}
# c.add(2)
# c.clear()
# for i in range(10):
#     c.add(i)
# c.add(2)
# print(c)

# a=["ism", 45, 78.36]
# print(a[0])
# for i in range(6):
#     a.append(i) # append- list oxiriga qo'shib beradi.
# print(a)

# for i in range(6):
#     a.insert(1, i) # insert- aytilgan indexga qo'shib beradi.
# print(a)

# a=["ism", 45, 78.36]
# a.pop(1) # berilgan indexdagi element ni olib tashlaydi.
# print(a)

# a.pop(a.index(45))
# print(a)

# dictinary - lug'atlar
# key : value - kalit so'z : uning qiymati

# d={
#     1: "bir",
#     2: "ikki",
#     3: "uch"
#     }
# a=int(input("sonni kiriting: "))
# print(d[a])

d={
    "apple": "olma",
    "book": "kitob"
}
# a=input("so'zni kiriting: ")

# eng=["apple", "book", "phone", "smart"]
# uzb=["olma", "kitob", "telefon", "aqlli"]
# c={}
# for i in range(len(eng)):
#     c[eng[i]] = uzb[i]
# print(c[a])
# c={}
# a="apple - olma"
# b=a.strip().split("-")
# c[b[0]]=b[1]
# print(c)
# c[b[0]]="banan"
# print(c)

eng=["apple", "book", "phone", "smart"]
uzb=["olma", "kitob", "telefon", "aqlli"]
c={}
for i in range(len(eng)):
    print(uzb[i])
a=c.values()
b=c.keys()
d=c.items()

print(a)
print(b)
print(d)
for i in c.items():
    print(i)
s= 2,43,54, (23,32)
s=s.index((23, 32))
print(type(s), s)