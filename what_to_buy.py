"""
Write a program that receives three inputs (given):

 A list of prices
A list of item names
A budget per item
 
The program should print:
A list of items that you can afford within your budget
How much budget would you need if you bought all of the affordable items
How many items you couldn't afford
"""

prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
total_needed = 0
cant_afford = 0

# Write your code below
for indx in range(len(prices)):             # len(prices) == len(items)
    if prices[indx] <= budget_per_item:     # --> prices[indx] belongs to items[index]
        affordable_items.append(items[indx])
        total_needed += prices[indx]

cant_afford = len(items) - len(affordable_items)



print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
