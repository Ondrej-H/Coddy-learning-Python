n = int(input())

if n % 2 == 1 and 1 <= n < 1000:
    for i in range(1, n + 1, 2):
        print(i * "*")

        