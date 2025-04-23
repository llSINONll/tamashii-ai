'''
#Challenge_1 (Monster Combo Maker)
#✅ Your Task:
You have a list of monsters.
Each monster has:
"name"
"element"
"abilities" (list of attack names)
🔧 Your job:
Loop through every pair of monsters (don’t pair a monster with itself).
Create a combo name using:
Their names: "Goblin + Slime Combo"
Their elements: "Earth + Water"
One ability from each (e.g. "Quick Attack + Power Strike")

Print the combo move like this:
Goblin + Slime Combo:
Elements: Earth + Water
Abilities: Quick Attack + Power Strike
📦 Example monsters list:
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

for i in range(len(monsters)):
    for j in range(i+1, len(monsters)):
        name1 = monsters[i]['name']
        name2 = monsters[j]['name']
        print(f"{name1} + {name2} Combo:")
        print(f"Elements: {monsters[i]['element']} + {monsters[j]['element']}")
        print(f"Abilities: {monsters[i]['abilities'][0]} + {monsters[j]['abilities'][0]} \n")
'''

#Challenge_2 (Fusion Monster Creator)

'''
⚔️ Scenario:
You’re now building fusion monsters from pairs of existing ones.
Each fusion should have:
A name made by combining both monster names with a hyphen (-)
An element combo made the same way
A special ability: the last ability of each monster joined with a +
The fusion is saved into a new list called fusion_monsters

✅ Your Task:
Create and print fusion monsters using this format:

Name: Goblin-Dragon  
Element: Earth-Fire  
Special Ability: Quick Attack + Ultimate Blast  
🧪 Start with this monster list:

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

combo_list = []

for i in range(len(monsters)):
    for j in range(i+1, len(monsters)):
        combo_monster = {}
        combo_name = monsters[i]['name']+'-'+monsters[j]['name']
        combo_element_name = monsters[i]['element']+'-'+monsters[j]['element']
        combo_ability_name = monsters[i]['abilities'][len(monsters[i]['abilities'])-1]+' + '+monsters[j]['abilities'][len(monsters[j]['abilities'])-1]
        combo_monster["combo_name"] = combo_name
        combo_monster["combo_element"] = combo_element_name
        combo_monster["combo_ability"] = combo_ability_name
        combo_list.append(combo_monster)

for monster in combo_list:
    print(f"Name: {monster['combo_name']}")
    print(f"Element: {monster['combo_element']}")
    print(f"Ability: {monster['combo_ability']} \n")


'''

















