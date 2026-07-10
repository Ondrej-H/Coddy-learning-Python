def print_sequence(n):
    # Write code here
    if n < 1:
        print("Blast off!")
        return

    print(f"T-minus {n}")
    print_sequence(n - 1)


print_sequence(3)