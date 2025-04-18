'''
#Challenge_1 Inventory Tracker (List of Dicts)
#You are given an RPG inventory where each item is a dictionary containing its name and quantity.
#inventory = [
#   {"item": "Potion", "quantity": 3},
#    {"item": "Elixir", "quantity": 2},
#    {"item": "Sword", "quantity": 1}
#]
#🧙 Your Task:
#
#Loop through the list and print out each item and its quantity like:
#Potion x3  
#Elixir x2  
#Sword x1

inventory = [
   {"item": "Potion", "quantity": 3},
    {"item": "Elixir", "quantity": 2},
    {"item": "Sword", "quantity": 1}
]

for item in inventory:
    i = item
    print(f"{i['item']} x{i['quantity']}")
'''

'''
#Challenge_2: (Battle Log Parser)
#You’re given a list of battle logs. Each log is a string in the format:
#"Character - Action - Target"

#🧙 Example:
#battle_log = [
#  "Kirito - Attacked - Goblin",
#  "Asuna - Healed - Kirito",
#  "Sinon - Shot - Dragon"
#]
#✅ Your Task:
#Loop through each log.
#Split the log string into character, action, and target.
#Print it nicely like:
#Kirito performed Attacked on Goblin
#Asuna performed Healed on Kirito
#Sinon performed Shot on Dragon

battle_log = [
  "Kirito - Attacked - Goblin",
  "Asuna - Healed - Kirito",
  "Sinon - Shot - Dragon"
]


for log in battle_log:
    s_log = log.split(" - ")
    print(f"{s_log[0]} performed {s_log[1]} on {s_log[2]}")
'''

'''
#Challenge_3: Loot Combiner
#You’re given two lists:
#One with item names
#One with corresponding quantities
#Example:
#loot_items = ["Potion", "Elixir", "Sword"]
#loot_counts = [3, 2, 1]
#🧙‍♂️ Your Task:
#Combine these into a list of dictionaries where each dictionary looks like:
#{"item": "Potion", "quantity": 3}
#Print the final list.
#✅ Expected Output:
#[
#  {'item': 'Potion', 'quantity': 3},
#  {'item': 'Elixir', 'quantity': 2},
#  {'item': 'Sword', 'quantity': 1}
#]


loot_items = ["Potion", "Elixir", "Sword"]
loot_counts = [3, 2, 1]

items_list = []
for items, counts in zip(loot_items, loot_counts):
    items_dict = {}
    items_dict['item'] = items
    items_dict['quantity'] = counts
    items_list.append(items_dict)
print(items_list)
'''
