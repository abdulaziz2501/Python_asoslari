#"""False, None, True, and, as, assert, async, await, break, 
#class, continue, def, del, elif, else, expect, finally, for,
#from, global, if, import, in, is, lambda, nonlocal, not, or, pass, 
#raise, return, try, while, with, yield""" ushbu so'zlardan 
#o'zgaruvchi nomi sifatida foydalanib bo'lmaydi, chunki bu so'zlar pythonning maxsus keywordlaridir

#String methods

#"""
#sense="lonely and alone. the exam is approaching"
#print(sense.title()) # title() stringdagi har bitta so'zni birinchi harfini katta harfga aylantiradi
#print(sense.capitalize()) # capitalize() stringdagi birinchi so'zning birinchi harfini katta harfga aylantiradi
#"""
#split()
#rsplit()
#lsplit()
#upper()
#lower()

#19-functions

#def -> create function 

#def hello ():
#    #salom beruvchi funksiya
#    print("good morning")
#hello()


#def hello(name):
#    print(f"good afternoon, {name.title()}")
#hello('ali')


#def count_age(name, year):
#    print(f"{name.title()} is {2023-year} years old") 
#count_age("muxtor", 2003)


#def age(birth_year=2003, moment_year=2023):
#    print(f"{moment_year-birth_year} yoshdasiz")
#age()

#19-amaliyot-function
#m-1
#def age (name, yosh):
#    print(f"{name.title()} {2023-yosh}-yilda tug'ilgansiz")
#age('ali', 21)

#m-2
#def num(a):
#    print("kvadrati = ", a*a, "kubi = ", a**3)
#num(int(input("Enter num: ")))

#m-3
#def num(a):
#    if a%2==0:
#        print("juft")
#    else:
#        print("toq")
#num(int(input("enter num: ")))

#m-4
#def loo(a, b):
#    if a>b:
#        print("Max=", a)
#    if a<b:
#        print("Max=", b)
#    if a==b:
#    print("sonlar teng")
#loo(12, 12 )

#m-5
#def pow(x, y):
#    print(x**y)
#pow(2, 6)

#m-7. Foydalanuvchidan son qabul qilib, 
#sonni 2 dan 10 gacha bo'lgan sonlarga
#qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 

#def lop(a):
#    for i in range(2, 11):
#        if a%i==0:
#            print(f"{a} {i} ga qoldiqsiz bo'linadi")
#lop(70)




#20-Qiymat qaytaruvchi funksiyalar

#def full_name(name, surname):
#    full_name=f"{name} {surname}"
#    return full_name
#student1=full_name ("Timur", "Alixanov")
#student2=full_name ("Nodir", "Anvarov")
#print(f"Darsga kelmagan talabalar {student1} va {student2}")


#def full_name(name, surname, f_name=''):
#    if f_name:
#        names=f"{name} {f_name} {surname}"
#    else:
#        names=f"{name} {surname}"
#    return names.title()
#student1=full_name('timur', 'alixanov')
#student2=full_name('rashid', 'kamilov', 'ilhomovich')
#print(f"Darsga kelmagan studentlar: {student1} va {student2}")

"""
import colorama as c

def car(company, brend, color, piece=None):
    avto={'kompaniyasi':company,
          'brendi' :brend,
          'rangi':color,
          'narxi':piece}
    return avto

car1=car("Bugatti", "Bugatti Chiron", "Blue")
car2=car("Ferrari", "Ferrari GTX250", "Red", 220000)
car3=car("GM", "Gentra", "White", 20000)
cars=[car1, car2, car3]
print("Cars on the online market")
for i in cars:
    if i ['narxi']:
        piece = i ['narxi']
    else:
        piece = "None"
    print(c.Fore.RED + f"{i ['rangi']} {i ['brendi']}--> Narxi: {piece}")
"""

"""
#2 ta son oralig'idagi sonlarni list ko'rinishida chiqarish
def oraliq (min, max ):
    num = [] # empty list
    while min<=max:
        num.append(min)
        min+=1
    return num
print(oraliq (0, 10))
print(oraliq(11, 20))
"""



"""
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input(" Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    print(avtolar)
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
   
"""


#8-Ro'yxatlar.

#cars=['marcedes', 'bugatti', 'audi', 'lamborgini', 'malibu']
#cars.sort(reverse=True)
#print(sorted(cars, reverse=True))

#num = list((range(1, 10, 2))) #range func. bilan ma'lum oraliqdagi sonlarni olishimiz mumkin. range(a, b, c) --> a=start, b=stop, c=step
#print(num)


"""
narxlar = [11, 15, 20, 23, 25, 28, 30]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print ("Eng arzon narx = ", arzon, ".Eng qimmat narx = ", qimmat, ".Jami narx = ", jami)

"""


#9-For sikli
"""
mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
for mehmon in mehmonlar:
    print ("salom", mehmon)
"""

#mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
#for mehmon in mehmonlar:
#    print ("salom", mehmon)
#    print ("xayr", mehmon)

#mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
#for mehmon in mehmonlar:
#    print ("Hurmatli", {mehmon}, "aka, sizni 20- iyun kuni ertalab, soat 08:00 dagi nahorgi oshga taklif qilamiz"  )

#sonlar = list(range(1, 11))
#for son in sonlar:
#    print (f"{son} ning kvadrati {son**2} ga teng")

"""
sonlar = list(range(1, 11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)\

print (sonlar)
print (sonlar_kvadrati)
"""

"""
friends = []
print("5 ta do'stingiz kim?")
for i in range  (5):
    friends.append(input(f"{i+1} - do'stingizni kiriting: "))

print(friends)
"""

#10-if-else --> Tarmoqlanish

#avtolar = ['audi', 'kia', 'hyundai', 'volvo', 'bmw']
#for avto in avtolar:
#    if avto ==  'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())


#login = input("Enter login: ")
#if len(login)<6:
#    print ("Login uzunligi 6 tadan kam bo'lishi mumkin emas!")
"""
yil = int( input ("Enter year: "))
if 2023-yil<18:
    print (f"Siz {2023-yil} yoshda ekansiz")
    print ("Siz uchun kirish mumkin bo'lmagan sayt!")
else:
    print ("Welcome!")
"""

"""
yosh = int (input("Yoshingizni kiriting: "))
if yosh<4:
    piece=0
elif yosh<18:
    piece=350
elif yosh<30:
    piece=500
else:
    piece=800 

print(f"Siz {piece} ming to'laysiz")
"""

"""
menu = ['osh', 'shashlik', 'norin', 'somsa', 'kabob']
food = input ("choice foods: ")
if food.lower() in menu:
    print("buyurtma qabul qilindi")
else:
    print("hozircha bunday food mavjud emas")
"""

#14-Dictionary


#car = {'model': 'Bugatti', 'color': 'Black'}
#print (car['model'], car['color'])



#talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tu'gilgan,\
# {talaba_0['yosh']} yoshda")

#15-Lug'at elementlari bilan ishlash

"""
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())



for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")

"""

"""
friends = {
    'Elboy': 'samsung s9',
    'Samar': 'poco X3',
    'Ilyos': 'samsung S 21 ultra',
    'Akobir': 'iphone X'
}

for name, phone in friends.items():
    print(f"{name.title()} ning telefoni {phone}")
"""

"""
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

print(" ")
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
"""

""" 
python = {
    'boolean': 'mantiqiy qiymat',
    'float': "o'nlik son",
    'integer': 'butun son',
    'for': 'biror amalni qayta-qayta bajaruvchi tsikl',
    'if': 'shartlarni tekshiruvchi operator'
}

print("Python's dictionary: ")
for i, j in python.items():
    print (f"{i.title()} -> {j}")
"""


#16-Nesting. tarmoqlanish



#17-While tsikli

#num =1
#while num <5:
#    print(num, end=' ')
#    num +=1

"""
print ("Kiritilgan sonning kvadratini qaytaruvchi dastur")
son = "son kiriting va dasturni to'xtatish uchun 'exit' ni kiriting: "

ishora = True
while ishora:
    qiymat = input(son)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)

print("stop program")

"""


"""
def kvadratga_oshirish(sonlar):
    kvadratlar = []
    for son in sonlar:
        kvadrat = son ** 2
        kvadratlar.append(kvadrat)
    return kvadratlar

raqamlar = [1, 2, 3, 4, 5]
natija = kvadratga_oshirish(raqamlar)
print(natija)Agar siz bir fayl ichidagi so'zlarni sanashni bilishni ist

"""


"""
# Lambda funksiyasiga misol:
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))
"""


"""
# 1 dan 10 gacha sonlarning ildizini qaytaruvchi dastur
from math import sqrt
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)
"""


"""
# Filter funksiyasi
random orqali 100 gacha sonlardan 10 tasini olib, ularni faqat juftlarini qaytaruvchi funkiya

import random as r

sonlar = r.sample(range(100),10) 


def juftmi(x):
    
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)
"""














































