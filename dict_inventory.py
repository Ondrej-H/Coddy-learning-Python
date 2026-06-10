"""
Create a function named update_inventory that takes three parameters:
inventory_dict (a dictionary), item (a string), and quantity (an integer).
The function should update the inventory_dict with the new item and quantity.
If the item already exists in the inventory,
its quantity should be increased by the given amount.
If the item does not exist, a new item should be added with the given quantity.
The function should return the updated dictionary.
"""


def update_inventory(inventory_dict, item, quantity):
    if item not in inventory_dict:
        inventory_dict[item] = quantity

    if item in inventory_dict:
        inventory_dict[item] += quantity

    return inventory_dict