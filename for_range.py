# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for num in range(30, 81):
    if num % 4 == 0:
        print(num, end = ", ")


print()  # Creates a new line for better readability

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
num = 15
for i in range(8):
    print(num, end=", ")
    num += 2


print()  # Creates a new line for better readability

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for num in range(50, 9, -1):
    if num % 5 == 0:
        print(num, end=", ")


print()  # Creates a new line for better readability

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
# Remember: print only the number, not "Product = number"
num = 1
for i in range(1, 31):
    if i % 3 == 0:
        num *= i
print(num)


