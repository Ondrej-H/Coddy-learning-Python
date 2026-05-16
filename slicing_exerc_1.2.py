"""
Create a program that receives a list as input (given) and 
prints the following sliced list (depends on the list length):

For odd-length lists: take the middle item and one item on each side (3 items total)
For even-length lists: take the two middle items
When dividing numbers:

/ gives you a decimal number (5/2 = 2.5)
// removes the decimal part (5//2 = 2)
For this challenge, use // because list slicing only works with whole numbers.
"""

lst = input().split(",")
#lst = [10, 20, 30, 40, 50, 60]

sliced_list = []

if len(lst) > 1 :
    if len(lst) % 2 == 1:
        sliced_list.append(lst[(len(lst) // 2) -1])
        sliced_list.append(lst[len(lst) // 2])
        sliced_list.append(lst[(len(lst) // 2) + 1])

    elif len(lst) % 2 == 0:
        sliced_list.append(lst[(len(lst) // 2) -1])
        sliced_list.append(lst[len(lst) // 2])
    
    print(sliced_list)

else:
    print(lst)

    