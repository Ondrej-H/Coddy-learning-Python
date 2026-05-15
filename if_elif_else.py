level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line
level_message = "None" # Don't change this line

# Write your code below
if has_training == "False" or has_training == "false":
    has_training = False

if 1 <= level <= 5:
    level_message = "Basic weapons only"
elif (6 <= level <= 10) and not has_training:
    level_message = "Need weapon training first"
elif (6 <= level <= 10) and has_training:
    level_message = "Access to advanced weapons granted"
elif level >= 11:
    level_message = "Access to all weapons granted"
else:
    level_message = "Invalid level"

# Don't change below this line
print(level_message)