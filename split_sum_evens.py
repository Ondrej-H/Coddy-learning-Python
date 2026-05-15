numbers = input().split(',')
# Write your code below
sum_evens = 0
for char in numbers:
    num = int(char)
    if num % 2 == 0:
        sum_evens += num

print(sum_evens)
