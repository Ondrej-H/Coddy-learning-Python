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

#lst = input().split(",")
lst = [10, 20, 30, 40, 50, 60]

def extract_list_middle(lst):
    if len(lst) % 2 == 1:
        lst_mid = lst[(len(lst) // 2) - 1 : (len(lst) // 2) + 2]
    else:
        lst_mid = lst[(len(lst) // 2) - 1 : (len(lst) // 2) + 1]

    return lst_mid

print(extract_list_middle(lst))