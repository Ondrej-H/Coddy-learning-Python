""""
Create a program that takes a list and prints:

For lists with 5 or more items: the first two and last two items
For lists with less than 5 items: the first and last item only
"""

#input_list = input().split(', ')
input_list = [10, 20, 30, 40]
# Write your code below

def extract_list(lst):
    if len(lst) >= 5:
        extracted_list = lst[:2] + lst[-2:]
    else:
        extracted_list = [lst[0], lst[-1]]
    return extracted_list


print(extract_list(input_list))