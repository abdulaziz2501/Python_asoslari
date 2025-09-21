from os import system, path
from math import *
system("clear")




# registratsiya
# login



class Tarmoq:
    def __init__(self):
        self.name = None
        self.username = None
        self.email = None
        self.password = None
        self.choose = [0, 1, 2]
    
    def registration(self):
        self.name = (input("Name: ")).strip()
        if len(self.name) < 4:
            while len(self.name) < 4:
                self.name = (input("Again enter name: ")).strip()

        self.username = (input("Username: ")).strip()
        if len(self.username) < 4:
            while len(self.username) < 4:
                self.username = (input("Again enter username: ")).strip()

        self.email = (input("Email: ")).strip()
        if len(self.email) < 4:
            while len(self.email) < 4:
                self.email = (input("Again enter email: ")).strip()

        self.password = (input("Password: ")).strip()
        if len(self.password) < 4:
            while len(self.password) < 4:
                self.password = (input("Again enter password: ")).strip()

        ind = 1
        if path.exists("users.txt"):
            file = open("users.txt", "r+")
            ind = len(file.readlines()) + 1
            file.write(f"\n{ind}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        else:
            file = open("users.txt", "a")
            file.write(f"{1}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        self.clear()

        print("""
            Login [1]
            chiqish [2]
            """)
        tanlov = int(input("select 1 or 2: "))

        if tanlov == 1:
            self.login()
        elif tanlov == 2:
            self.chiqish()
        else:
            exit("Xato tanlov")

    


    def login(self):
        print("Login")

        self.name = (input("Name: ")).strip()
        self.username = (input("Username: ")).strip()
        self.email = (input("Email: ")).strip()
        self.password = (input("Password: ")).strip()


        tanlov1 = int(input("username ni yangilaysizmi yoki password ni? 1/0: "))
                
        if tanlov1 == 1:
            self.username2=input("New username: ")
            if self.username2==self.username:
                print("Username yangilanmadi, qolgan urinishlar soni 1 ta, iltimos qaytadan yangi username kiriting: ")
                self.username2=input("New username: ")
            if not self.username2==self.username:
                print("Username muvaffaqqiyatli almashtirildi.")
            else:
                print("Urinishlar soni tugadi, keyinroq yana urinib ko'ring!")

        if tanlov1==0:
            self.password2=input("New password: ")
            if self.password2==self.password:
                print("Password yangilanmadi, qolgan urinishlar soni 1 ta, iltimos qaytadan yangi password kiriting: ")
                self.password2=input("New password: ")
            if not self.password2==self.password:
                print("Password muvaffaqqiyatli almashtirildi.")
            else:
                print("Urinishlar soni tugadi, keyinroq yana urinib ko'ring!")


        ind = 1
        if path.exists("users.txt"):
            file = open("users.txt", "r+")
            ind = len(file.readlines()) + 1
            file.write(f"\n{ind}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        else:
            file = open("users.txt", "a")
            file.write(f"{1}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        



    def kirish(self):
        self.clear()
        print(''' 
            Registratsiya [0]
            Login [1]
            Chiqish [2]
        ''')
        tanlov = int(input("Tanlang: "))
        self.clear()
        if not tanlov in self.choose:
            exit("Xato tanlov")
        if tanlov == self.choose[0]:
            self.registration()
        elif tanlov == self.choose[1]:
            self.login()
        else:
            self.chiqish()

    def chiqish(self):
        exit("Tizimdan chopildik")
    
    def clear(self):
        system("clear")



one = Tarmoq()

one.kirish()



































































