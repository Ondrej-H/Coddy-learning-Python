"""
Create a program that takes two inputs: 
a string of numbers separated by spaces, and a prefix string. 
The program should split the number string into individual numbers,
add the prefix to each number, 
then join these modified numbers
back into a single string separated by spaces.
Finally, print the resulting string.
"""

numbers = input()
prefix = input()
# Write your code below

numbers_list = numbers.split()
prefixed_numbers_lst = []

for number in numbers_list:
    prefixed_number = prefix + number
    prefixed_numbers_lst.append(prefixed_number)
    result = " ".join(prefixed_numbers_lst)

print(result)
