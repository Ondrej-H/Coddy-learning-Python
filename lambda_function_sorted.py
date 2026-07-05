def dictionary_sorter(data_dict: dict):
    # Use sorted() to sort the dictionary items by their values
    # Hint: data_dict.items() returns (key, value) pairs
    # Hint: Use the 'key' parameter of sorted() to sort by value

    # Write code here
    print(list(data_dict.items()))
    print()
    print(sorted(data_dict.items()))
    print()

    sorted_dict = sorted(data_dict.items(), key=lambda item: item[1])
    return dict(sorted_dict)


dict1 = {'a': 3, 'b': 1, 'c': 2}

print(dictionary_sorter(dict1))
