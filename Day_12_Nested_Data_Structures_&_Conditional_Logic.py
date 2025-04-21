'''
#Challenge_1 (Monster Evolution Tracker)
#Scenario:
#You're managing a list of monsters in your RPG game.
#Each monster has a name, a level, and a list of abilities.
#As monsters gain experience, they level up and acquire new abilities.
#Your Task:
#Data Structure:
#Create a list named monsters containing dictionaries.
#Each dictionary should represent a monster with the following keys:
#"name": The monster's name (string).
#"level": The monster's current level (integer).
#"abilities": A list of the monster's abilities (list of strings).
#Level Up:
#Loop through each monster in the monsters list.
#Increase each monster's level by 1.
#Add New Ability:
#Based on the new level, add a new ability to the monster's abilities list:
#If the new level is 2, add "Quick Attack".
#If the new level is 3, add "Power Strike".
#If the new level is 4 or higher, add "Ultimate Blast".
#Display Updated Monsters:
#After updating, print each monster's name, new level, and list of abilities in a readable format.
#Example Output:

#Goblin - Level 2
#Abilities: Scratch, Quick Attack

#Dragon - Level 4
#Abilities: Flame, Roar, Ultimate Blast

#Slime - Level 3
#Abilities: Bounce, Split, Power Strike

monsters = [
    {"name": "Goblin", "level": 1, "abilities": ["Scratch"]},
    {"name": "Dragon", "level": 3, "abilities": ["Flame", "Roar"]},
    {"name": "Slime", "level": 2, "abilities": ["Bounce", "Split"]}
    ]

for monster in monsters:
    monster["level"] += 1
    print(f"{monster['name']} - Level {monster['level']}")
    if monster["level"] == 2:
        monster["abilities"].append("Quick Attack")
        print("Abilities:" , ", ".join(monster["abilities"]))
    elif monster["level"] == 3:
        monster["abilities"].append("Power Strike")
        print("Abilities:" , ", ".join(monster["abilities"]))
    elif monster["level"] >= 4:
        monster["abilities"].append("Ultimate Blast")
        print("Abilities:" , ", ".join(monster["abilities"]))
'''    


'''
#Challenge_2 (Monster Inventory Swap)
#Scenario:
#You are now managing an inventory system for monsters.
#Each monster has a list of items they own,
#and you need to perform an inventory swap.
#Each monster can trade a certain number of items with another monster.
#Your goal is to swap the items between two monsters
#while keeping track of what each monster owns after the trade.
#Task:
#You are given two monsters with their respective inventories:
#monsters = [
#    {"name": "Goblin", "inventory": [{"item": "Potion", "quantity": 5}, {"item": "Sword", "quantity": 2}]},
#    {"name": "Dragon", "inventory": [{"item": "Elixir", "quantity": 3}, {"item": "Shield", "quantity": 1}]}
#]
#Your task is to:
#Swap items between Goblin and Dragon.
#After the swap, print the new inventory of each monster.
#Swap Logic:
#Swap Potion with Elixir.
#Swap Sword with Shield.
#Expected Output:
#Goblin's Inventory:
#Elixir x3
#Shield x1

#Dragon's Inventory:
#Potion x5
#Sword x2

monsters = [
    {"name": "Goblin", "inventory": [{"item": "Potion", "quantity": 5}, {"item": "Sword", "quantity": 2}]},
    {"name": "Dragon", "inventory": [{"item": "Elixir", "quantity": 3}, {"item": "Shield", "quantity": 1}]}
]

def swap_inventory(monster_1, monster_2):
    monster_1["inventory"], monster_2["inventory"] = monster_2["inventory"], monster_1["inventory"]

swap_inventory(monsters[0], monsters[1])

def display_inventory(monster):
    print(f"\n{monster['name']}'s Inventory:")
    for item in monster["inventory"]:
        print(f"{item['item']} x{item['quantity']}")

display_inventory(monsters[0])  
display_inventory(monsters[1])  
'''
