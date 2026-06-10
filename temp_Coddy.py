def frequency_counter(data_list):
    # Write code here
    dict_counts_of_elements = {}
    for element in data_list:
        dict_counts_of_elements[element] = data_list.count(element)

    return dict_counts_of_elements


lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(frequency_counter(lst))