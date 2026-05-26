# Read two integers for the power calculation
num1 = int(input())
num2 = int(input())

# TODO: Calculate num1 raised to the power of num2
powered =  num1 ** num2

# Then find the leading (first) digit of the result
# Hint: Convert the result to a string to access the first digit
string_powered = str(powered)
leading_digit = int(string_powered[0])

print(leading_digit)

# Read the text message
message = input()

# TODO: Rearrange the message by moving consonants to the beginning
# Keep vowels (a, e, i, o, u - both uppercase and lowercase), spaces, and punctuation after them
# Maintain the original order within each group
# Hint: You might want to create two separate strings - one for consonants and one for everything else
consonants = "bcdfghjklmnpqrstvwxyz"
message_consonants = []
message_rest = []

for char in message:
    if char.lower() in consonants:
        message_consonants.append(char)
    else:
        message_rest.append(char)


rearranged = "".join(message_consonants) + "".join(message_rest)  # Replace with your rearranged message

print(rearranged)