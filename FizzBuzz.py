# my solution
print("Welcome to FizzBuzz!")

def fizzbuzz(num=21):
    num = int(num)
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 7 == 0:
        return "Buzz"
    else:
        return str(num)


num = input()
print(fizzbuzz(num))