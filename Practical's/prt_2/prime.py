# n = 100
# count = 0
# for x in range(1,101):
#     if  x % n== 0:
#         count += 1
#         sum = x 
#     if count == 2:
#         print(sum)

n = int(input("Enter the number:"))
count =0
for x in range (1,n+1):
    if n % x == 0:
        count += 1
        sum = n
if count == 2:
    print("Given number is a prime number")
    print(sum)
else:
    print("not a prime")