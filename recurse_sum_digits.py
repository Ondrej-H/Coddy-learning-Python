# Coddy solution - better
def sum_digits(n):
    if n < 10:  # Base case
        return n
    else:  # Recursive step
        return (n % 10) + sum_digits(n // 10)


# my solution
def sum_digits(n):
    # Write code here
    if len(str(n)) == 1:
        return n
    
    return int(str(n)[-1]) + sum_digits(n // 10)

print(sum_digits(1234))