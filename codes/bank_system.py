
class BankAccaunt:
    def __init__(self, account_number, balance):
        self.__account_number=account_number
        self.__balance=balance

    def __init__(self, account_number, initial_balance):
        pass

    def deposite(self, amount):
        self.__balance +=amount

    def withdraw(self, amount):
        if amount<self.__balance:
            self.__balance -=amount

    def get_balance(self):
        return self.__balance


class Customer:
    def __init__(self, customer_id, name, email):
        self.__customer_id=customer_id
        self.__name=name
        self.__email=email
        self.__accaunt = None

    def __init__(self, customer_id, name, email):
        pass

    def open_account(self, inital_balance):
       
        bank_akk = BankAccaunt(202, 0)
        self.__accaunt = bank_akk
        return bank_akk


    def close_account(self, account_number):
        .

    def get_account_balance(self, account_number):
        return account_number

    def depost_to_account(self, account_number, amount):
        return amount

    def withdraw_from_account(self, account_number, amount):
        return amount

    


class Bank:
    def __init__(self):
        self.__accaunt_list = []
        

    def add_customer(self, customer):
        accaunt = customer.open_account(0)
        self.__accaunt_list.append(accaunt)

    def remove_customer(self, customer_id):
        for i in self.__accaunt_list:
            

    def get_customer_accounts(self, customer_id):
        pass

    def transfer_funds(self, from_account_number, to_account_number, amount):
        pass


mijoz1=BankAccaunt(100000000001, 5000)
customer1=Customer(100, "Muxtor", "Muxtor23@gmail.com")

























