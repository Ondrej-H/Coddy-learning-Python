def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            # TODO: Recursively call sum_nested on the sublist and add to total
            total += sum_nested(element)
            pass
        else:
            # TODO: Add the integer directly to total
            total += element
            pass
    return total


nested_list = [1, [2, 3], [4, [5, 6]], 7]

print(sum_nested(nested_list) )