list_of_lists = [[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]
#= [[1, 2], [3, 4],[10, 20],[20, 40], [60, 80]]


less_than_50_lists = [lst for lst in list_of_lists if sum(lst) <= 50]
print(less_than_50_lists)

#less_than_5 = []
'''for lst in list_of_lists:
    for num in lst:
        if num < 5:
            less_than_5.append(num)'''

# same as:
less_than_5 = [num for lst in less_than_50_lists for num in lst if num < 5]

# same as:
less_than_5 = [
    num
    for lst in less_than_50_lists
    for num in lst
    if num < 5
    ]

print(less_than_5)