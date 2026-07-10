
'''
Write a recursive function named count_down that takes a
positive integer n as an argument and prints each number from
n down to 0
'''

def count_down(n):
    # Write code here
    if n < 0:
        return
    
    print(n)

    count_down(n - 1)


count_down(3)