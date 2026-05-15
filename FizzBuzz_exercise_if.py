# best solution
"""
Uprav pravidla:

místo 3 → 5
místo 7 → 9
Almost Fizz → třeba 'Almost Buzz'
"""

def fizzbuzz(num):
    if num % 5 == 0 and num % 9 == 0:
        return "FizzBuzz"
    
    if num % 5 == 0:
        return "Fizz"
    
    if num % 9 == 0:
        return "Buzz"
    
    if "9" in str(num):
        return "Almost Buzz"
    
    return str(num)

number = int(input("Insert a number: "))
for each_number in range(1, number +1):
    print(fizzbuzz(each_number))

