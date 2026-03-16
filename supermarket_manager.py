# Project: Supermarket Inventory Manager
# Concept: List Modification (Add/Remove elements)

suber_market = ["milk", "bread", "eggs"]

# User input to identify what to change
switch = input("Enter the item you want to switch: ")
new_item = input("Enter the name of the new item: ")

# Logical steps to update the list
suber_market.remove(switch)
suber_market.append(new_item)

print(f"Updated Inventory: {suber_market}")
