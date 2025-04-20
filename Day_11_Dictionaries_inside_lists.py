'''
#Challenge_1 (Monster Hunter Inventory Update)

#You are tasked with updating an inventory system.
#In the given list of dictionaries, each dictionary represents
#a monster's item with its name and quantity.
#Your goal is to loop through the list and update the quantity of each
#item by adding 1 to it, and then print the updated inventory.
#Monster Inventory Example:
#inventory = [
#    {"item": "Potion", "quantity": 5},
#    {"item": "Elixir", "quantity": 3},
#    {"item": "Sword", "quantity": 1}
#]
#Expected Output:
#Potion x6  
#Elixir x4  
#Sword x2

inventory = [
    {"item": "Potion", "quantity": 5},
    {"item": "Elixir", "quantity": 3},
    {"item": "Sword", "quantity": 1}
]

for item in inventory:
    item['quantity'] += 1
    print(f"{item['item']} x{item['quantity']}")
'''

'''
#Challenge_2 (Monster Skill Updater)
#You're now managing monsters who each have a name
#and a list of skills. Each skill has a name and a level.
#You're given a list like this:
#monsters = [
#    {"name": "Goblin", "skills": [{"name": "Scratch", "level": 1}, {"name": "Bite", "level": 2}]},
#    {"name": "Dragon", "skills": [{"name": "Flame", "level": 5}, {"name": "Roar", "level": 4}]},
#    {"name": "Slime", "skills": [{"name": "Bounce", "level": 1}, {"name": "Split", "level": 1}]}
#]
#✅ Your Task:
#Loop through each monster
#For each skill, increase the level by 1
#Print the updated skills in the format:
#Goblin's Skills:
#- Scratch (Level: 2)
#- Bite (Level: 3)

#Dragon's Skills:
#- Flame (Level: 6)
#- Roar (Level: 5)

#Slime's Skills:
#- Bounce (Level: 2)
#- Split (Level: 2)

monsters = [
    {"name": "Goblin", "skills": [{"name": "Scratch", "level": 1}, {"name": "Bite", "level": 2}]},
    {"name": "Dragon", "skills": [{"name": "Flame", "level": 5}, {"name": "Roar", "level": 4}]},
    {"name": "Slime", "skills": [{"name": "Bounce", "level": 1}, {"name": "Split", "level": 1}]}
]

for monster in monsters:
    print(f"\n{monster['name']}'s Skills:")
    skill_list = monster['skills']
    for skills in skill_list:
        skills['level'] += 1
        print(f"- {skills['name']} (Level: {skills['level']})")
'''

'''
#Final_Challenge (Inventory Merger Combine loot from different Monsters)
#You're given two separate monster inventories.
#Each inventory is a list of dictionaries containing items and quantities.
#inventory_1 = [
#    {"item": "Potion", "quantity": 2},
#    {"item": "Elixir", "quantity": 1},
#    {"item": "Sword", "quantity": 1}
#]

#inventory_2 = [
#    {"item": "Potion", "quantity": 3},
#    {"item": "Elixir", "quantity": 2},
#    {"item": "Shield", "quantity": 1}
#]
#✅ Your Task:
#🧠 Combine both inventories into one final inventory.
#If an item appears in both, add their quantities.
#If an item is unique to one list, just include it as is.

#✅ Final Output Format:
#Potion x5  
#Elixir x3  
#Sword x1  
#Shield x1


inventory_1 = [
    {"item": "Potion", "quantity": 2},
    {"item": "Elixir", "quantity": 1},
    {"item": "Sword", "quantity": 1}
]

inventory_2 = [
    {"item": "Potion", "quantity": 3},
    {"item": "Elixir", "quantity": 2},
    {"item": "Shield", "quantity": 1}
]

merged_inventory = {}

for item in inventory_1:
    name = item['item']
    qty = item['quantity']
    merged_inventory[name] = qty

for item in inventory_2:
    name = item['item']
    qty = item['quantity']
    if name in merged_inventory:
        merged_inventory[name] += qty
    else:
        merged_inventory[name] = qty

for item, qty in merged_inventory.items():
    print(f"{item} x{qty}")
'''
