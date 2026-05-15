lst = list(map(int, input().split(",")))
# Write your code below
lst_of_indices = []

def sort_out_indexes(lst):
    for index, value in enumerate(lst):

        if value < 50 or value % 5 == 0:
            lst_of_indices.append(index)

    return lst_of_indices


print(sort_out_indexes(lst))