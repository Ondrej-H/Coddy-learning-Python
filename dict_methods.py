my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)
# Output: dict_keys(['name', 'age', 'city'])

values = my_dict.values()
print(values)
# Output: dict_values(['Alice', 30, 'New York'])

items = my_dict.items()
print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

"""
get(key, default): Returns the value for the specified key.
If the key is not found,
it returns the default value (or None if no default is specified).
"""
age = my_dict.get('age')
print(age)
# Output: 30

country = my_dict.get('country', 'USA') # 'USA' is default
print(country)
# Output: USA

# pop(key): Removes the element with the specified key and returns its value.
city = my_dict.pop('city')
print(city)
# Output: 'New York'
print(my_dict)
# Output: {'name': 'Alice', 'age': 30}