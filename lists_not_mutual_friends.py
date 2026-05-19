"""
Create a function called not_mutual_friends that takes
two lists of names representing two people's friend lists.
The function should return a list of names that are friends with
only one person (not mutual friends).

Let's say we have:

Person A's friends: ["John", "Emma", "Mike", "Sarah"]
Person B's friends: ["Emma", "Tom", "Sarah", "Peter"]
When we call not_mutual_friends with these two lists, it should return:
["John", "Mike", "Tom", "Peter"]

Explanation:

"John" and "Mike" are only friends with Person A
"Tom" and "Peter" are only friends with Person B
"Emma" and "Sarah" are mutual friends (friends with both people),
so they are not included in the result
"""

def not_mutual_friends(list1, list2):
    # Write your code below
    result_friends = []

    for friend in list1:
        if friend not in list2:
            result_friends.append(friend)

    for friend in list2:
        if friend not in list1:
            result_friends.append(friend)
    
    return result_friends


lst1 = ["John", "Emma", "Mike", "Sarah"]
lst2 = ["Emma", "Tom", "Sarah", "Peter"]

print(not_mutual_friends(lst1,lst2))