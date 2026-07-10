def factorial(n):
    if n == 1: # Base case
        return 1

    previous = factorial(n - 1) # Recursive call
    result = n * previous

    print(f"{n} * {previous} = {result}")

    return result


print(f"Result: {factorial(5)}") # Output: 120