def reverse(lst):
    # Write code here
    reversed_list = []
    for element_index in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[element_index])
    
    return reversed_list


list1 = [1, 2, 3]
print(reverse(list1))