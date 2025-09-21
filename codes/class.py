# # class Telefon():
# #     def __init__(self, model, kamera, xotira, yili, rangi):
# #         self.brend=model
# #         self.camera=kamera
# #         self.memory=xotira
# #         self.year=yili
# #         self.color=rangi
        
        
# # class Samsung(Telefon):
    
    
# #     def muddati(self):
# #         yaroqlilik=2023-self.year
# #         if yaroqlilik<3:
# #             return True
# #         else:
# #             return False
# #     def price(self):
# #         narx=self.camera*5+self.memory*10
        
# #         if self.color=="oq":
# #             narx=self.camera*5+self.memory*10+narx*1.5
# #             return narx
# #         elif self.color=="qora":
# #             narx=self.camera*5+self.memory*10+narx*2
# #             return narx

            
# #     def konsol(self):
# #         print(self.brend, self.camera, self.memory, self.year, self.color, self.muddati(), self.price())
                    
            
# # phone=Samsung("Samsung", 108, 512, 2021, "qora")
# # phone.konsol()


# # class Train():
# #     def __init__(self, number, direction, date, time):
# #         self.raqam=number
# #         self.boshqaruv=direction
# #         self.sana=date
# #         self.vaqt=time
        
# #     def __str__(self):
# #         return (f"{self.raqam}-poyezd {self.boshqaruv}ga {self.sana}-kuni {self.vaqt} da yo'lga chiqadi")
        
# # poyezd1=Train(212, "Nagoya", "16.09.2023", "07:00")
# # poyezd2=Train(21232, "London", "15.09.2023", "08:00")
# # poyezd3=Train(21212, "Berlin", "11.09.2023", "09:00")
# # poyezd4=Train(23112, "Madrid", "17.09.2023", "10:00")
# # poyezd5=Train(456212, "Moskva", "15.09.2023", "19:00")
# # poyezd6=Train(2412, "New York", "15.09.2023", "20:00")
# # poyezd7=Train(21632, "Paris", "15.09.2023", "21:00")
# # poyezd8=Train(21532, "Rim", "15.09.2023", "22:00")


# # poeyzdlar = [poyezd1,poyezd2, poyezd3, poyezd4, poyezd5, poyezd6, poyezd7, poyezd8]

# # for p in poeyzdlar:
# #     if "11" == p.sana.split('.')[0]:
# #         print(p)



# # class Telefon():
# #     def __init__(self, model, kamera, xotira, yili, rangi):
# #         self.brend=model
# #         self.camera=kamera
# #         self.memory=xotira
# #         self.year=yili
# #         self.color=rangi
        
        
# # class Samsung(Telefon):
    
    
# #     def muddati():
# #         yaroqlilik=2023-self.year
# #         if yaroqlilik<3:
# #             return True
# #         else:
# #             return False
# #     def price():
# #         narx=self.camera*5+self.memory*10
        
# #         if self.color=="oq":
# #             narx=self.camera*5+self.memory*10+narx*1.5
# #             return narx
# #         else:
# #             if self.color=="qora":
# #                 narx=self.camera*5+self.memory*10+narx*2
# #                 return narx
# #         else:
# #             return narx
            
# #     def konsol():
# #         print(self.brend, self.camera, self.memory, self.year, self.color)
                    
            
# # phone=Samsung("Samsung", 108, 512, 2021, "qora")
# # phone.konsol()


# # class Train():
# #     def __init__(self, number, direction, date, time):
# #         self.raqam=number
# #         self.boshqaruv=direction
# #         self.sana=date
# #         self.vaqt=time
        
# #     def __str__(self):
# #         print(f"{self.raqam}-poyezd, {self.boshqaruv}ga, {self.sana}-kuni, {self.vaqt} da yo'lga chiqadi")
        
# # poyezd=Train(212, "Nagoya", "15.09.2025", "09:00")
# # poyezd.__str__()


# # class Flight():
# #     def __init__(self, seat_count):
# #         self.set_count=seat_count
# #         self.passangers=[]
        
# #     def is_empty(self):
# #         if self.set_count>0 and len(self.passangers) < self.set_count:
# #             return True
# #         else:
# #             return False
            
# #     def add_passangers(self,passanger):
# #         if self.is_empty():
# #             self.passangers.append(passanger)
# #             print("qo'shildi")
# #         else:
# #             print("qo'shilmadi")
        
# # class Passangers():
# #     def __init__(self, first_name, last_name):
# #         self.name1=first_name
# #         self.name2=last_name

# # flight1=Flight(4)
# # passanger1=Passangers("Ali", "Olimov")
# # passanger2=Passangers("Vali", "Alimov")
# # passanger3=Passangers("Nodir", "Botirov")
# # passanger4=Passangers("Daler", "Alisherov")
# # passanger5=Passangers("Ahmad", "Shamsiyev")
# # pass_list=[passanger1, passanger2, passanger3, passanger4, passanger5]

# # for i in pass_list:
# #     flight1.add_passangers(i)



# class Avto():
#     def yoqilgi(self):
#         pass

# class Ferrari(Avto):
#     def yoqilgi(self):
#         print("benzin")

# class Tank(Avto):
#     def yoqilgi(self):
#         print("kerosin")

# class Malibu(Avto):
#     def yoqilgi(self):
#         print("propan")

# ferrari=Ferrari()
# ferrari.yoqilgi()

# tank=Tank()
# tank.yoqilgi()

# malibu=Malibu()
# malibu.yoqilgi()




# class Person():
#     def tepish(self, obj1):
#         print("Odam tepganda ")
#         obj1.uchish()

# class Koptok():
#         def uchish(self):
#             print("koptok uchadi")

# person=Person()
# koptok=Koptok()
# person.tepish(koptok)


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Myaauuuvvv")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Vaaaavvvvvvvv")


# class Wolf:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#              print(f"I am a wolf. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#             print("uuuuvvvvvv")

        
# class Snake:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#          print(f"I am a snake. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("fssssssssss")


# class Frog:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#          print(f"I am a frog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("vaq vaq")



# class Cow:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#          print(f"I am a cow. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Muuuuuuuu")

    
# class Owl:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def info(self):
#          print(f"I am a owl. My name is {self.name}. I am {self.age} years old.")


#     def make_sound(self):
#         print("Kukku kukku")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)
# wolf1=Wolf("Albert", 5)
# snake1=Snake("Ninza", 8)
# frog1=Frog("Bark", 3)
# cow1=Cow("Masha", 9)
# owl1=Owl("Kane", 7)

# for animal in (cat1, dog1, wolf1, snake1, frog1, cow1, owl1):
#     animal.info()
#     animal.make_sound()





























