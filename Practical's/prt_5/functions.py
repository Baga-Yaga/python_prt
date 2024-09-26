num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

def fun_add(a,b):
    return a + b
def fun_sub(a,b):
    return a - b
def fun_mul(a,b):
    return a * b
def fun_div(a,b):
    return a / b
def fun_mod(a,b):
    return a % b

print(f'\nAddition: {fun_add(num1,num2)}')
print(f'Substraction: {fun_sub(num1,num2)}')
print(f'Multiplication: {fun_mul(num1,num2)}')
print(f'Division: {fun_div(num1,num2)}')
print(f'Modulus: {fun_mod(num1,num2)}')


add = lambda n1,n2: n1 + n2
sub = lambda n1,n2: n1 - n2
mul = lambda n1,n2: n1 * n2
div = lambda n1,n2: n1 / n2
mod = lambda n1,n2: n1 % n2

print("\nlambda function :- ")
print(f'Addition: {add(num1,num2)}')
print(f'Substraction: {sub(num1,num2)}')
print(f'Multiplication: {mul(num1,num2)}')
print(f'Division: {div(num1,num2)}')
print(f'Modulus: {mod(num1,num2)}')

# print the even numbers from the list
