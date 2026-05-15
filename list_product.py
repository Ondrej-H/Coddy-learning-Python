def prod(lst):
    # Write code here
    result = 1
    for element in lst:
        result *= element
    return result


first_list = [1, 2, 3]
print(prod(first_list))