# # class Student:
# #     def info(self):
# #         print("Hello")
# #
# # st=Student()
# # st.info()
#
#
# class Addition():
#     def adder(self,a,b):
#         return "Addition of a + b = ",a+b
#
#     def substract(self,a,b):
#         return "Subtraction of a - b = ",a-b
#
#     def multiply(self,a,b):
#         return "Multiplication of a * b = ",a*b
#
#     def divide(self,a,b):
#         return "Division of a / b = ",a/b
#
#
# a = int(input("Enter num1 : "))
# b = int(input("Enter num2 : "))
# ad= Addition()
# print(ad.adder(a,b))
# print(ad.substract(a,b))
# print(ad.multiply(a,b))
# print(ad.divide(a,b))


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} has balance {self.balance}")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def __del__(self):
        print("account object is been destroyed!")

a = int(input("Enter account number: "))
b = int(input("Enter balance: "))
my_account = BankAccount(a,b)
my_account.check_balance()

del my_account
