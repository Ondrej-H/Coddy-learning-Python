"""
Write a program that finds all pairs of numbers that multiply to give n using numbers from 1 to n (inclusive).
The program should show all possible combinations, including duplicate pairs in reverse order.
For example, both "1 6" and "6 1" should be shown, as they are considered different arrangements of the same pair.
Numbers can also be paired with themselves if their product equals n.

Important: Only consider numbers in the range from 1 to n. If n is less than 1, no pairs exist.
"""

# my solution
n = int(input())
# Write your code below
for i in range(1, n+1):
    #i * x == n
    if n % i == 0:
        n2 = n / i
        print(f"{i} {int(n2)}")


# nested for solution
n = int(input())
# Write your code below
for i in range(1, n+1): # od 1, abys se netiskla nula, kdyby byl input 0
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)