def combine_and_filter(lst, threshold):
    # Write code here
    result_list = []
     
    for element in lst:
        if element > threshold:
            result_list.append(element)
    
    result_list.sort()

    return result_list


list1 = [1, 5, 3, 2, 7, 4]
#treshold = 3
print(combine_and_filter(list1, 3))
