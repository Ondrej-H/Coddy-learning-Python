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
nums = numbers.split()
result_nums  = []
for num in nums:
    result_nums.append(prefix + num)
result = ' '.join(result_nums)
print(result)