'''
#Challenge_1 (Search an Inventory)
# Create a list of items like ["Potion", "Shield", "Sword"]
# Ask the player to input an item name
# If the item is in the inventory, print "You already have it!"
# Else, print "You need to find it!"

inventory = ["Potion", "Shield", "Sword"]
item = input("Enter an item to search: ")
if item.lower() in [i.lower() for i in inventory]:
    print(f"You already have it!! {item}")
else:
    print("You need to find it!")
'''

'''
#Challenge_2 (Dictionary Lookup Game)
# Create a dictionary of spells and their MP cost
# Example: {"Fireball": 30, "Heal": 20, "Teleport": 50}
# Ask user to enter a spell name
# If the spell exists, print its MP cost
# Else, say "Unknown Spell"

spells = {"Fireball": 30, "Heal": 20, "Teleport": 50}

s_name = input("Enter the spell name: ")
# Check if the spell exists (case-insensitive)
if s_name.title() in spells:
    print(f"The MP cost of {s_name.title()} is {spells[s_name.title()]}!")
else:
    print("Unknown Spell!")
'''

'''
#Challenge_3 (Count how many potions)
# You have an inventory list with multiple items including duplicates
# Count how many "Potion" you have and print it

inventory = ["Potion", "Sword", "Potion", "Shield", "Potion"]

count = 0
for i in inventory:
    if i == "Potion":
        count += 1
print(f"You have {count} no. of Potions")
'''
