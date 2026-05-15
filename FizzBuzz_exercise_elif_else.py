"""
Uprav pravidla:

místo 3 → 5
místo 7 → 9
Almost Fizz → třeba 'Almost Buzz'
"""

def fizzbuzz(num):
    if num % 5 == 0 and num % 9 == 0:
        return "FizzBuzz"
    
    elif num % 5 == 0:
        return "Fizz"
    
    elif num % 9 == 0:
        return "Buzz"
    
    elif "9" in str(num):
        return "Almost Buzz"
    
    else:
        return(str(num))


number = int(input())
for i in range(1, number + 1):
    print(FizzBuzz(i))


#print(FizzBuzz(number))