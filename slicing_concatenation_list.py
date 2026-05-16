"""
Create a program that receives a list of numbers as input and prints a new list that:

Contains the original list followed by its reverse
Has the first element of the original list inserted at the beginning and
 the last element inserted at the end
Repeats this entire sequence twice
For example:
1 2 3 → [1, 1, 2, 3, 3, 2, 1, 3, 1, 1, 2, 3, 3, 2, 1, 3]
"""

#numbers = input().split()
numbers = [1,2,3]
# Write your code below

def extend_list(lst):
    extended_list = ([lst[0]] + lst + lst[::-1] + [lst[-1]]) * 2
    return extended_list


print(extend_list(numbers))

"""
Coddy solution:

numbers = input().split()
reversed_numbers = numbers[::-1]
step1 = numbers + reversed_numbers
step2 = [numbers[0]] + step1 + [numbers[-1]]
step3 = step2 * 2
print(step3)
"""