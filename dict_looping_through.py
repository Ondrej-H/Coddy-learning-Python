# Looping through keys:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in my_dict:
    print(key)


# Looping through values:
for value in my_dict.values():
    print(value)


# Looping through key-value pairs:
# my_dict.items()
for key, value in my_dict.items():
    print(f'{key}: {value}')