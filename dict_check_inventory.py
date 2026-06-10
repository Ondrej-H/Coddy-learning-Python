def check_inventory(inventory, item):
    # Write code here
    if item in inventory:
        return f"{item} is in stock. Quantity: {inventory[item]}"
    
    else:
        return f"{item} is not in stock."