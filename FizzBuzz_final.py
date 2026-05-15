# better solution
print("Welcome to FizzBuzz!")

def fizzbuzz(limit):
    limit = int(limit)
    result = ""

    if limit % 3 == 0:
        result += "Fizz"

    if limit % 7 == 0:
        result += "Buzz"
        
    if result == "":
        result = str(limit)
    
    return result


limit = int(input())

# print(fizzbuzz(limit))

for number in range(1, limit + 1):
    print(fizzbuzz(number))