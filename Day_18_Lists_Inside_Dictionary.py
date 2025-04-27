#Challenge 1 (Monster Upgrade Inventory)
'''
🧩 Scenario:
Your Monster Lab 🧪 now tracks monster upgrades!
Each monster has a list of upgrades it can unlock.

✅ Your Task:
Add a new key `"upgrades"` to each monster in the list.
The upgrades should be a list of strings, like:

- Goblin: ["Steel Claws", "Earth Armor"]
- Dragon: ["Inferno Wings", "Blazing Tail"]
- Slime: ["Mega Bounce", "Tsunami Body"]

✅ Bonus:
After updating the monsters, print out each monster's name
and their list of upgrades.

🎯 Example Output:
Goblin can unlock: ['Steel Claws', 'Earth Armor']
Dragon can unlock: ['Inferno Wings', 'Blazing Tail']
Slime can unlock: ['Mega Bounce', 'Tsunami Body']
'''
'''
monsters = [
    {
        "name": "Goblin",
        "element": "Earth",
        "abilities": ["Scratch", "Quick Attack"]
    },
    {
        "name": "Dragon",
        "element": "Fire",
        "abilities": ["Flame", "Roar", "Ultimate Blast"]
    },
    {
        "name": "Slime",
        "element": "Water",
        "abilities": ["Bounce", "Split", "Power Strike"]
    }
]
for monster in monsters:
    if monster['name'] == "Goblin":
        monster["upgrades"] = ["Steel Claws", "Earth Armor"]
    elif monster['name'] == "Dragon":
        monster["upgrades"] = ["Inferno Wings", "Blazing Tail"]
    elif monster['name'] == "Slime":
        monster["upgrades"] = ["Mega Bounce", "Tsunami Body"]
    print(f"{monster['name']} can unlock: {monster['upgrades']}")
'''

#Challenge 2 (Upgrade Finder)
'''
🧩 Scenario:
Now that upgrades are added, you want a quick tool
to see if a monster has a specific upgrade!

✅ Your Task:
Write a function called has_upgrade(monster, upgrade_name).

The function should:
- Accept a monster dictionary and an upgrade name (string).
- Return True if the upgrade exists in their upgrades list, else False.

✅ Bonus:
Test the function with a few checks, like:

- Does Goblin have "Steel Claws"? → True
- Does Dragon have "Mega Bounce"? → False

🎯 Example:
has_upgrade(monster, "Steel Claws") → True or False
'''
'''
monsters = [
    {
        "name": "Goblin",
        "element": "Earth",
        "abilities": ["Scratch", "Quick Attack"],
        "upgrades": ["Steel Claws", "Earth Armor"]
    },
    {
        "name": "Dragon",
        "element": "Fire",
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "upgrades": ["Inferno Wings", "Blazing Tail"]
    },
    {
        "name": "Slime",
        "element": "Water",
        "abilities": ["Bounce", "Split", "Power Strike"],
        "upgrades": ["Mega Bounce", "Tsunami Body"]
    }
]


def has_upgrade(monster, upgrade_name):
    return upgrade_name in monster['upgrades']

# Testing
print("Testing:")
print("Goblin has Steel Claws?", has_upgrade(monsters[0], "Steel Claws"))  # True
print("Dragon has Mega Bounce?", has_upgrade(monsters[1], "Mega Bounce"))  # False
print("Slime has Tsunami Body?", has_upgrade(monsters[2], "Tsunami Body")) # True
'''
