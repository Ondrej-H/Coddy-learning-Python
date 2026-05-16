lst = input().split(",")
print(type(lst))
#lst = [2,4,6,8, 10]

# Write your code below
odd_lenght_list_items = []
even_len_list_items = []
one_or_less_item_in_list = []

if len(lst) > 1:
    if len(lst) % 2 == 1:
        middle_item_index = len(lst) // 2

        odd_lenght_list_items.append(lst[middle_item_index - 1])
        odd_lenght_list_items.append(lst[middle_item_index])
        odd_lenght_list_items.append(lst[middle_item_index + 1])
        
        print(odd_lenght_list_items)


    elif len(lst) % 2 == 0:
        even_len_list_items.append(lst[(len(lst) // 2) - 1])
        even_len_list_items.append(lst[len(lst) // 2])
        
        print(even_len_list_items)

    
else:
    print




