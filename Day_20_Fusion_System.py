#Challenge 1: Basic Monster Fusion
'''
🧩 Scenario:
Two monsters from your list can now fuse into one powerful hybrid! You’ll create a new monster that combines their abilities, element, and upgrades.

✅ Your Task:
Write a function called fuse_monsters(monster1, monster2).

The new fused monster should:

Have a name like "Fusion of Goblin & Dragon"

Combine the elements like "Earth/Fire"

Merge all abilities (no duplicates)

Merge all upgrades (no duplicates)

✅ Output Example:

{
  "name": "Fusion of Goblin & Dragon",
  "element": "Earth/Fire",
  "abilities": ["Scratch", "Quick Attack", "Flame", "Roar", "Ultimate Blast"],
  "upgrades": ["Steel Claws", "Earth Armor", "Inferno Wings", "Blazing Tail"]
}
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

def fuse_monsters(monster1,monster2):
    fused_monster = {"name": f"Fusion of {monster1['name']} & {monster2['name']}",
                     "element": f"{monster1['element']}/{monster2['element']}",
                     "abilities": list(set(monster1['abilities']+monster2['abilities'])),
                     "upgrades": list(set(monster1['upgrades']+monster2['upgrades']))
        }
    return fused_monster

fused_monster = fuse_monsters(monsters[0], monsters[1])
print(fused_monster)
'''
#Challenge_2 (Fusion Power Calculation)

'''
🧩 Scenario:
Now that you’ve fused monsters, it’s time to calculate their total fusion
power! The power is based on number of unique abilities and
elemental bonuses (same as before).

✅ Your Task:
Write a function called fusion_power(monster) that:
Counts unique abilities
Calculates the elemental bonus based on both elements in the fusion
Returns the total boosted power

✅ Boosts Reminder:
Earth → +10
Fire → +20
Water → +30
(Apply both if fusion has two elements)

✅ Formula:
boosted power = (unique abilities × 10) + element bonus

✅ Example:
For:
{
  "name": "Fusion of Goblin & Dragon",
  "element": "Earth/Fire",
  "abilities": ["Scratch", "Quick Attack", "Flame", "Roar", "Ultimate Blast"],
  ...
}
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

def fuse_monsters(monster1,monster2):
    fused_monster = {"name": f"Fusion of {monster1['name']} & {monster2['name']}",
                     "element": f"{monster1['element']}/{monster2['element']}",
                     "abilities": list(set(monster1['abilities']+monster2['abilities'])),
                     "upgrades": list(set(monster1['upgrades']+monster2['upgrades']))
        }
    return fused_monster

fused_monster = fuse_monsters(monsters[0], monsters[1])

def fusion_power(fused_monster):
    boosted_power = len(fused_monster['abilities'])*10
    elements = fused_monster['element'].split("/")

    for e in elements:
        if e == "Earth":
            boosted_power += 10
        elif e == "Fire":
            boosted_power += 20
        elif e == "Water":
            boosted_power += 30
    return boosted_power

fusion_power = fusion_power(fused_monster)
print(f"{fused_monster['name']} has total fusion power: {fusion_power}")
'''
