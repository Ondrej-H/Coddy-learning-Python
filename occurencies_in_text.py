text = input()
# Write your code below
seeked_char = "p"
occurencies = 0
for char in text.lower():
    if char == seeked_char:
        occurencies += 1

print(occurencies)