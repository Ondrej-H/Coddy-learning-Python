# better solution
print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    num = int(num)
    result = ""

    if num % 3 == 0:
        result += "Fizz"

    if num % 7 == 0:
        result += "Buzz"
        
    if result == "":
        result = str(num)
    
    return result


limit = input()
print(fizzbuzz(limit))