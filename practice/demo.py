'''

Sort a list:-

Create a function in Python that accepts two parameters.
The first will be a list of numbers.
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order.
If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
# '''

def Sort_by_order(num, order) :

    if order == 'asc':
        print(num.sort())
    elif order == 'desc':
         print(num.reverse())
    elif order == 'none':
        pass
    return num
#num = int(input('Enter the values: '))
num = input("enter teh values : ").split(',')
list1 = list(num)
list2 = int(list1)

order = input("Enter the order(asc,desc,none): ")

print(Sort_by_order(list2, order))

