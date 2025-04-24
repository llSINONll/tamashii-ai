'''
🧠 First, The Basics:
sorted() Function:
Used to sort lists (like our monsters list) without changing the original.

Syntax:
sorted(list, key=..., reverse=...)

key: a function that returns the value to sort by.

reverse=True: sorts in descending order.

💡 Lambda Function (Anonymous Function):
Instead of writing a separate function to use as key,
we can write it inline using lambda.

lambda monster: monster['name']
This grabs the 'name' value from each monster.
'''
'''
#Challenge_1 (Sort Alphabetically by Name)

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


sorted_by_name = sorted(monsters, key = lambda m: m['name'])
print(sorted_by_name)
for m in sorted_by_name:
    print(m['name'])
'''
'''
#Chellenge_2 (Sort by no. of abilities descending)

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

sorted_by_ability = sorted(monsters, key=lambda a: len(a['abilities']), reverse=True)
for a in sorted_by_ability:
    print(f"{a['name']} - {len(a['abilities'])} abilities")

'''
'''
#challenge_3 (Bonus): Sorted by Elements Alphabetically


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

sorted_by_element = sorted(monsters, key=lambda e: e['element'])
for e in sorted_by_element:
    print(f"{e['name']} - {e['element']}")
'''
'''
💡 #Challenge_4(Bonus): "Ability Mastery Counter"
🧩 Scenario:
You’re now building a Monster Training Center,
and you want to track how many abilities each monster has mastered.

Each monster has a name, element, and a list of abilities.

Your job:
🔹 Loop through all the monsters
🔹 For each monster, print their name and how many abilities they have
🔹 Add a new key called "ability_count" in each
monster's dictionary that stores this number

✅ Example Output:
Goblin has 2 abilities.
Dragon has 3 abilities.
Slime has 3 abilities.
And the monsters list should now include something like:

{
  "name": "Goblin",
  "element": "Earth",
  "abilities": ["Scratch", "Quick Attack"],
  "ability_count": 2
}
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

for m in monsters:
    m['ability_count'] = len(m['abilities'])
    print(f"{m['name']} has {m['ability_count']} abilities.")
'''

'''
#Challenge_5 (Sort the Monster!)
🧩 Scenario:
You’re building a Monster Encyclopedia,
and you want to list all monsters sorted alphabetically by
their name so trainers can find them easily.

✅ Your Task:
Use the sorted() function

Sort the monsters list by the "name" key

Print each monster’s name after sorting

🔍 Example Output:
Dragon  
Goblin  
Slime
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

sorted_by_name = sorted(monsters, key=lambda m: m['name'])
for m in sorted_by_name:
    print(f"{m['name']}")
'''    
