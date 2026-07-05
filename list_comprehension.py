def sum_positive_evens(numbers):
    # Write code here
    positive_evens = [n for n in numbers if n > 0 and n % 2 == 0]
    return sum(positive_evens)
    # return sum([n for n in numbers if n > 0 and n % 2 == 0])

numbers = [-10, -5, 0, 2, 4, 7, 10, 12]

print(sum_positive_evens(numbers))