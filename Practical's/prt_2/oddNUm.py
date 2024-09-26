n = int(input("Enter the number:"))

for x in range(0,n):
    if x % 2 == 1:
        print(x)

sum =0
for x in range(0,n):
    if x % 2 == 1:
        sum += x

print("Sum of odd = "+sum)