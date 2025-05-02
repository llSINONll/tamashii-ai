'''
Common List Methods:
append(): Add an item to the end of the list.
extend(): Add all elements of an iterable to the list.
insert(): Insert an item at a given position.
remove(): Remove the first occurrence of a value.
pop(): Remove and return an item at a given position.
clear(): Remove all items from the list.
index(): Return the index of the first occurrence of a value.
count(): Return the number of times a value appears.
sort(): Sort the items of the list in place.
reverse(): Reverse the elements of the list in place.
copy(): Return a shallow copy of the list.
'''

#Challenge_1: Build a Monster Inventory System
'''
Scenario: You are developing a game where players
collect and manage a list of monsters.
Each monster has attributes like name, type, and power level.

Tasks:
Create a List: Initialize a list to store monster dictionaries.
Add Monsters: Implement a function to add new monsters to the list.
Remove Monsters: Implement a function to remove a monster by name.
Display Monsters: Show all monsters in the inventory with their details.
Sort Monsters: Sort the list based on power level or name.
'''
'''
monsters = []

def add_monster(name, m_type, power):
    monster = {"name": name, "type": m_type, "power": power}
    monsters.append(monster)

def remove_monster(name):
    for monster in monsters:
        if monster["name"] == name:
            monsters.remove(monster)
            break

def display_monsters():
    for monster in monsters:
        print(f"Name: {monster['name']}, Type: {monster['type']}, Power: {monster['power']}")

def sort_monsters_by_power():
    monsters.sort(key=lambda x: x["power"], reverse=True)

    
add_monster("Goblin", "Earth", 50)
add_monster("Dragon", "Fire", 150)
display_monsters()
sort_monsters_by_power()
display_monsters()
remove_monster("Goblin")
display_monsters()
'''
    

#Challenge 2: Monster Squad Manager
'''
🧩 Scenario:
You are a monster trainer and need to manage a team (squad) of monsters. Each monster has a name, element, and power. You can only have 5 monsters in your squad at any time. Use list methods to manage this dynamic team!

✅ Your Tasks:
Initialize an empty monster_squad list.

Add Monsters to your squad using .append() if there’s room.

Remove Monsters by name using .remove().

Replace a monster using .insert() and .pop() or slicing.

Sort the squad by power using .sort() with a lambda.

Clear the squad using .clear().
'''
'''
monster_squad = []

def add_monster(name, element, power):
    if len(monster_squad) < 5:
        monster = {"name": name, "element": element, "power": power}
        monster_squad.append(monster)
        print(f"{name} added to the squad.")
    else:
        print("Squad is full! Remove a monster first.")

def remove_monster(name):
    for monster in monster_squad:
        if monster["name"] == name:
            monster_squad.remove(monster)
            print(f"{name} removed from the squad.")
            return
    print(f"{name} not found.")

def display_squad():
    for m in monster_squad:
        print(f"{m['name']} ({m['element']}) - Power: {m['power']}")

def sort_by_power():
    monster_squad.sort(key=lambda x: x["power"], reverse=True)
    print("Squad sorted by power.")

def clear_squad():
    monster_squad.clear()
    print("Squad cleared!")


add_monster("Goblin", "Earth", 80)
add_monster("Slime", "Water", 70)
add_monster("Dragon", "Fire", 120)
add_monster("Golem", "Earth", 100)
add_monster("Phoenix", "Fire", 150)

display_squad()

# Trying to add a 6th monster
add_monster("Fairy", "Air", 60)  # Should warn that squad is full

# Sort them by power
sort_by_power()
display_squad()

# Remove a monster
remove_monster("Slime")
display_squad()

# Add a new monster after removing one
add_monster("Fairy", "Air", 60)
display_squad()

# Clear the squad
clear_squad()
display_squad()
'''
