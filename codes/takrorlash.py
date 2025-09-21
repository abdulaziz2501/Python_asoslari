
# class MinutesConverter:
#     def __init__(self, minutes):
#         self.minutes=minutes

#     def toHours(self):
#         print( self.minutes / 60)

#     def toSeconds(self):
#         print ( self.minutes * 60)

#     def toDays(self):
#         print( self.minutes / (60*24))


# obj1=MinutesConverter(1440)
# obj1.toHours()
# obj1.toSeconds()
# obj1.toDays()

#####################################################



# class SpaceAircraft:
#     def __init__(self, model, height, fuel):
#         self.model = model
#         self.height = height
#         self.fuel = fuel

#     def launch(self, target_height):
#         fuel_needed = target_height - self.height
#         if fuel_needed > self.fuel:
#             print("No fuel")
#         else:
#             self.height = target_height
#             self.fuel -= fuel_needed
#             print("Launched to height:", self.height)

#     def land(self, target_distance):
#         fuel_needed = target_distance / 1000
#         if fuel_needed > self.fuel:
#             print("No fuel")
#         else:
#             self.fuel -= fuel_needed
#             print("Landed at distance:", target_distance)


# obj1=SpaceAircraft("Airways", 200, 4000)
# obj1.launch()
# obj1.land()



# class MyList(list):
#     def remove(self, value):
#         while value in self:
#             super().remove(value)

# my_list = MyList([1, 2, 2, 3, 4, 2, 5])
# print(my_list) 

# my_list.remove(2)
# print(my_list)























