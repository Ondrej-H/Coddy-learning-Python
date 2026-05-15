# Why is a while loop better than a for loop for finding the smallest power of 2 greater than a number?
# defining variables
number = 27
power_of_2 = 1

# while loop
while power_of_2 <= number:
    power_of_2 *= 2

print(power_of_2)


# for loop
for _ in range(number):   # maximálně 27 pokusů
    if power_of_2 > number:
        break
    power_of_2 *= 2

print(power_of_2)

# Proto je zde lepší while
# Vím počet opakování, nebo jen podmínku konce?
# -> počet opakování -> for loop
# -> podmínku konce -> while loop
