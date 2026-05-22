"""
Create a function named find_occurrences that:

Takes two string arguments: text and pattern
Counts how many times pattern appears in text, including overlapping occurrences
Returns a tuple containing:
A boolean indicating if the pattern was found (True/False)
The number of occurrences of the pattern
A list of starting positions where the pattern was found
For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

If the pattern is not found, return (False, 0, []).

About the pass keyword: You'll see pass in the default code. It's a Python keyword that means "do nothing" and is used as a placeholder when Python requires an indented code block (like inside a function). You should replace pass with your actual function code.
"""


def find_occurrences(text, pattern):
    # Write your code here    
    pattern_found = False
    if pattern in text:
        pattern_found = True

    occurencies = 0
    starting_positions = []
    for i in range(len(text) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurencies += 1
            starting_positions.append(i)

    return pattern_found, occurencies, starting_positions


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result) 