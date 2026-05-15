# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
for row in range(rows):
    # Inner loop for columns
    line = ""
    for col in range(cols):
        line += "*"
    print(line)