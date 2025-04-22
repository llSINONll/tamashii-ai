'''
Previous Dictionary things to know:

Accessing nested dictionary values
my_dict = {"monster": {"name": "Goblin", "level": 2}}
print(my_dict["monster"]["name"])  # Output: Goblin


Updating dictionary values
my_dict["monster"]["level"] += 1

Adding a new key-value pair
my_dict["monster"]["element"] = "Fire"

Removing a key from a dictionary
del my_dict["monster"]["element"]

Looping through dictionaries
for key, value in my_dict.items():
    print(f"{key}: {value}")
'''

'''
Challenge_1 (Monster Element Enchanter)
⚔️ Scenario:
Your RPG monsters are getting elemental upgrades!
You now need to assign an elemental type to each monster and update their data.

✅ Your Task:
You have a list of monsters.
Each monster has:
"name": The monster's name.
"level": Its level.
"abilities": A list of its powers.

Assign an element to each monster based on its name:
If "Goblin" → "Earth"
If "Dragon" → "Fire"
If "Slime" → "Water"
Any other → "Neutral"

Add a new key "element" to each monster's dictionary with the appropriate value.

📌 Example Input:
monsters = [
    {"name": "Goblin", "level": 2, "abilities": ["Scratch", "Quick Attack"]},
    {"name": "Dragon", "level": 4, "abilities": ["Flame", "Roar", "Ultimate Blast"]},
    {"name": "Slime", "level": 3, "abilities": ["Bounce", "Split", "Power Strike"]}
]
✅ Expected Output:

Goblin (Earth) - Level 2
Abilities: Scratch, Quick Attack

Dragon (Fire) - Level 4
Abilities: Flame, Roar, Ultimate Blast

Slime (Water) - Level 3
Abilities: Bounce, Split, Power Strike

'''
'''
monsters = [
    {"name": "Goblin", "level": 2, "abilities": ["Scratch", "Quick Attack"]},
    {"name": "Dragon", "level": 4, "abilities": ["Flame", "Roar", "Ultimate Blast"]},
    {"name": "Slime", "level": 3, "abilities": ["Bounce", "Split", "Power Strike"]}
]

for monster in monsters:
    if monster['name'] == "Goblin":
        monster['element'] = "Earth"
    elif monster['name'] == "Dragon":
        monster['element'] = "Fire"
    elif monster['name'] == "Slime":
        monster['element'] = "Water"
    else:
        monster['element'] = "Neutral"
    abilities = ", ".join(monster['abilities'])
    print(f"{monster['name']} ({monster['element']}) - Level {monster['level']}")
    print(f"Abilities: {abilities}\n")
'''

'''
#Challenge_2 (Elemental Inventory Tracker)

🧩 Scenario:
Now that your monsters have elements, let’s make their inventory element-themed.
Each monster has an inventory list with items. You’ll customize their items based on their element type!

✅ Your Task:
Start with this modified list of monsters (with element and inventory):

monsters = [
    {
        "name": "Goblin",
        "level": 2,
        "abilities": ["Scratch", "Quick Attack"],
        "element": "Earth",
        "inventory": ["Rock", "Leaf"]
    },
    {
        "name": "Dragon",
        "level": 4,
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "element": "Fire",
        "inventory": ["Ash", "Flame Gem"]
    },
    {
        "name": "Slime",
        "level": 3,
        "abilities": ["Bounce", "Split", "Power Strike"],
        "element": "Water",
        "inventory": ["Droplet", "Seaweed"]
    }
]
🧠 Logic:
Loop through each monster and:

Display the monster’s name and element

Print their inventory items like this:

Goblin (Earth)
Inventory: Rock, Leaf

Dragon (Fire)
Inventory: Ash, Flame Gem

Slime (Water)
Inventory: Droplet, Seaweed
'''
'''
monsters = [
    {
        "name": "Goblin",
        "level": 2,
        "abilities": ["Scratch", "Quick Attack"],
        "element": "Earth",
        "inventory": ["Rock", "Leaf"]
    },
    {
        "name": "Dragon",
        "level": 4,
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "element": "Fire",
        "inventory": ["Ash", "Flame Gem"]
    },
    {
        "name": "Slime",
        "level": 3,
        "abilities": ["Bounce", "Split", "Power Strike"],
        "element": "Water",
        "inventory": ["Droplet", "Seaweed"]
    }
]

for monster in monsters:
    inventory = ", ".join(monster['inventory'])
    print(f"{monster['name']} ({monster['element']})")
    print(f"Inventory: {inventory}\n")
'''
'''
#Challenge_Bonus (Elemental Combo Crafter)

🧩 Scenario:
Every monster now has elemental affinity and based on that,
they craft a combo move using their abilities.
You’ll generate a new string called "combo_move" for each monster,
based on their element and their abilities.

✅ Your Task:
Loop through the monsters.

Based on their element, generate a combo move:
🌍 Earth → Join abilities with " & Smash → "
🔥 Fire → Join abilities with " + Blaze → "
💧 Water → Join abilities with " ~ Splash → "
⚪ Neutral → Just join with " -> "

Add the combo as a new key called "combo_move" in each monster dictionary.

Then print this:
Goblin (Earth)
Combo Move: Scratch & Smash → Quick Attack
'''
'''
monsters = [
    {
        "name": "Goblin",
        "level": 2,
        "abilities": ["Scratch", "Quick Attack"],
        "element": "Earth",
        "inventory": ["Rock", "Leaf"]
    },
    {
        "name": "Dragon",
        "level": 4,
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "element": "Fire",
        "inventory": ["Ash", "Flame Gem"]
    },
    {
        "name": "Slime",
        "level": 3,
        "abilities": ["Bounce", "Split", "Power Strike"],
        "element": "Water",
        "inventory": ["Droplet", "Seaweed"]
    },
    {
        "name": "Mimic",
        "level": 5,
        "abilities": ["Mimicry", "Shadow Bite"],
        "element": "Neutral",
        "inventory": ["Gold Coin", "Rusty Key"]
    }
]

for monster in monsters:
    print(f"{monster['name']} ({monster['element']})")
    if monster['element'] == "Earth":
        combo = " & Smash → ".join(monster["abilities"])
    elif monster['element'] == "Fire":
        combo = " + Blaze → ".join(monster["abilities"])
    elif monster['element'] == "Water":
        combo = " ~ Splash → ".join(monster["abilities"])
    else:
        combo = " -> ".join(monster["abilities"])

    monster["combo_move"] = combo
    
    print(f"Combo Move: {monster['combo_move']}\n")
'''
