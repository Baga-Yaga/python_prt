
n = int(input("Enter the number:"))
for x in range(0,n):
    if x % 2 == 0:
        print(x)


sum = 0
for x in range(0,n):
    if x % 2 == 0:
        sum += x
        

print("sum of even = ",sum)