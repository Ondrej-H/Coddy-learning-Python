"""
Create a program that receives a list as input (given) and
 prints three new lists based on the following slicing operations:

A list containing every third element, starting from index 1 (the second element)
A list containing all the elements from the 6th element to the 1st in reverse order
A list containing every second element starting from the middle of the list to the end
"""

#lst = input().split(",")
lst = [10, 20, 30, 40, 50, 60, 70, 80]
# Write your code below

def extract_3_lists(lst):
    lst1 = lst[1::3]
    lst2 = lst[5::-1]
    lst3 = lst[(len(lst) // 2)::2]
    return f"{lst1}\n{lst2}\n{lst3}"

print(extract_3_lists(lst))