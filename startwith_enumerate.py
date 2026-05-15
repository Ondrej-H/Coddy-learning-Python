"""
Write a program that receives a list of words as input (given),
and prints a list of the indices of the words that are 
either longer than 3 characters 
or start with the letter 'a' (case-sensitive).

To check if a string starts with some substring use: 
str.startswith("substring")
"""

# without str.startwith() method
lst = input().split()
# Write your code below
indexes_lst = []
for index, word in enumerate(lst):
    if len(word) > 3 or word[0].lower() == "a":
        indexes_lst.append(index)

print(indexes_lst)


# str.startwith() method used
lst = input().split()
# Write your code below
indexes_lst = []
for index, word in enumerate(lst):
    if len(word) > 3 or word.startswith("a".lower()):
        indexes_lst.append(index)

print(indexes_lst)

