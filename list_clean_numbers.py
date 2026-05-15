# odstraní čísla <= 0 a sudá čísla
# vrátí nový seřazený list
def clean_numbers(lst):
    result_list = []

    for element in lst:
        if element % 2 != 0 and element > 0:
            result_list.append(element)
    
    result_list.sort()

    return result_list

        
list1 = [2, 13, 4, -6, 5, 6, 0, 8, 9]
print(clean_numbers(list1))