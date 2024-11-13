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
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance {self.balance}.")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def __del__(self):
        print(f"Account {self.account_number} is being closed.")


# Menu-driven program
a = int(input("Enter account number: "))
b = int(input("Enter initial balance: "))
my_account = BankAccount(a, b)

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        my_account.check_balance()
    elif choice == "2":
        deposit_amount = int(input("Enter amount to deposit: "))
        my_account.deposit(deposit_amount)
    elif choice == "3":
        withdraw_amount = int(input("Enter amount to withdraw: "))
        my_account.withdraw(withdraw_amount)
    elif choice == "4":
        print("Exiting the program.")
        del my_account
        break
    else:
        print("Invalid choice. Please select a valid option.")
