"""
Create a program that receives two lists and
prints a new list of all elements that are in the first list but NOT in the second list.
"""

lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below

def diference_lists(lst1, lst2):
    result_list = []

    for element in lst1:
        if element not in lst2:
            result_list.append(element)
    
    return result_list


print(diference_lists(lst1, lst2))