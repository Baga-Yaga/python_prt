a = input("Enter :")
b = ""
for x in a[-1::-1]:
    b+=x

print("Palindrome = "+b)

if b == a:
    print(f"{a} is a palindrome")

else:
    print("not a palindrome")
