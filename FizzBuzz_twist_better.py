# my solution
print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    number = int(number)
    result = ""

    if number % 3 == 0:
        result += "Fizz"

    if number % 7 == 0:
        result += "Buzz"

    if number % 3 != 0 and number % 7 != 0:
        if "3" in str(number):
            result = "Almost Fizz"

    if result == "":
        result = str(number)
    
    return result


limit = int(input())

# print(fizzbuzz(limit))

for num in range(1, limit + 1):
    print(fizzbuzz(num))