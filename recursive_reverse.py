def recursive_reverse(s):
    if len(s) <= 1:  # Base case: empty or single-character string
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]  # Recursive step

text = "ab"
result = recursive_reverse(text)
print(result)
# Output: olleh