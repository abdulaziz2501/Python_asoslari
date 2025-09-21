# Sinf ishi: W-1

# class Son:
#     def __init__(self, son):
#         self.son = son
        
#     def kvadrat(self):
#         return self.son ** 2
    
#     def ildiz(self):
#         return self.son ** 0.5
    
#     def kub(self):
#         return self.son ** 3
    
#     @staticmethod
#     def yigindi(a, b):
#         return a + b
    
#     @staticmethod
#     def ayirma(a, b):
#         return a - b
    
#     @staticmethod
#     def kopaytma(a, b):
#         return a * b
    
#     @staticmethod
#     def bolindi(a, b):
#         if b == 0:
#             return "Nolga bo'lib bo'lmaydi"
#         else:
#             return a / b
        
# son1 = Son(5)
# print(son1.kvadrat())
# print(son1.ildiz())
# print(son1.kub())

# son2 = Son(7)
# print(Son.yigindi(son1.son, son2.son))
# print(Son.ayirma(son1.son, son2.son))
# print(Son.kopaytma(son1.son, son2.son))
# print(Son.bolindi(son1.son, son2.son))

################################################
# Sinf ishi: Avtomobil classi

# class Avto():
#     def __init__(self, model, dvigatel_work, position_fuel ):
#         self.model=model
#         self.__dvigatel_work=dvigatel_work
#         self.__position_fuel=position_fuel


#     def get_model(self):
#         print("Bugatti Chiron")

#     def get_dvigatel(self):
#         print("norm")

#     def get_position(self):
#         print("me'yorida")

# car=Avto("Bugatti Neyron", "zo'r", "ko'p")
# car.get_model()
# car.get_dvigatel()
# car.get_position()

#################################################3

#Uyga vazifa: Avtomobil

# class Avto():
#     def __init__(self, brend, position):
#         self.brend=brend
#         self.position=position
        

#     def car_active(self):
#         self.car_active=input("Car_active: yoniq/o'chiq: ")
#         if self.car_active=="o'chiq":
#             print("Mashina yurmaydi, chunki dvigetel o'chiq")
#         else:
#             print("Mashina yuradi")
            

#     def car_fire(self):
#         pass

#     def car_distance(self):
#         self.distance=int(input("Enter car_distance: "))
#         print(f"Masofa: {self.distance} ")
        

#     def car_fuel(self):
#         self.fuel=int(input("Enter car_fuel: "))
#         if self.fuel<self.distance:
#             print(f"Yoqilg'i: {self.fuel}")
#             print("Mashina yurmaydi. ")
#         else:
#             print("Yo'lingiz bexatar bo'lsin.")

        

#     def car_position(self):
#         if self.fuel<=100:
#             print("Hammasi joyida")
#         else:
#             print("Alert! Alert! Alert!")


# car=Avto("Bugatti", "New")
# car.car_active()
# car.car_distance()
# car.car_fuel()
# car.car_position()














































