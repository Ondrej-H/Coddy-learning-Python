def change_element(list1, index, list2):
    # Write your code below
    list1[index] = list2[0]
    return list1


first_list = [1, 2, 3]
second_list = [5, 6, 7]
print(change_element(first_list, 1, second_list))