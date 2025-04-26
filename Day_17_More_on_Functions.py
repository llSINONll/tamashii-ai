#Challenge 1 (Monster Power Calculator)
'''
🧩 Scenario:
You're the head scientist at the Monster Lab 🧪,
and you want to calculate the power level of a
monster based on how many abilities it has.

✅ Your Task:
Write a function called calculate_power(monster)
It should accept one monster dictionary (like Goblin, Dragon, etc.)
The power level = number of abilities × 10
The function should return the calculated power level.
✅ Bonus:
After defining the function, loop through all monsters and print:

"{Monster Name} has a power level of {Power Level}"

🧠 Example:

Goblin has 2 abilities → 2×10 = 20
Output → Goblin has a power level of 20

Dragon has 3 abilities → 3×10 = 30
Output → Dragon has a power level of 30

Here's your monster list again:
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
def calculate_power(monster):
    power_level = len(monster['abilities'])*10
    return power_level

for monster in monsters:
    power_level = calculate_power(monster)
    print(f"{monster['name']} has a power level of {power_level}")
'''
#Challenge 2 (Elemental Power Boost)
'''
🧩 Scenario:
You’re continuing your work at the Monster Lab 🧪,
but this time you're adding a cool new feature:
Elemental Power Boost. Each monster's power level
should be modified based on their element.

Earth monsters get a +10 boost.

Fire monsters get a +20 boost.

Water monsters get a +30 boost.

Your job: 🔹 Write a function calculate_power_with_boost(monster) that will:

Accept a monster dictionary (like Goblin, Dragon, etc.).

Calculate the power level (abilities count × 10).

Add an elemental power boost based on the monster's element.

Return the final boosted power level.

Then, loop through all monsters and print:

{Monster Name} has a power level of {Power Level} with
boost of {Boosted Power Level}
Example:
Goblin (Earth) has 2 abilities → 2 × 10 = 20 → Boost = +10 → Final = 30

Dragon (Fire) has 3 abilities → 3 × 10 = 30 → Boost = +20 → Final = 50

Slime (Water) has 3 abilities → 3 × 10 = 30 → Boost = +30 → Final = 60

Here’s the starting monster list again:

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
def calculate_power_with_boost(monster):
    power_level = len(monster['abilities']) * 10
    if monster['element'] == "Earth":
        power_level += 10
    elif monster['element'] == "Fire":
        power_level += 20
    elif monster['element'] == "Water":
        power_level += 30
    return power_level

for monster in monsters:
    boosted_power = calculate_power_with_boost(monster)
    base_power = len(monster['abilities'])*10
    print(f"{monster['name']} has a power level of {base_power} with boosted power of {boosted_power}")
'''
#Challenge 3 (Ultimate Monster Profile)
'''
🧩 Scenario:
You're upgrading the Monster Lab 🧪 again!
This time you want a complete monster profile that includes everything:
the monster’s name, element, number of abilities, base power, and boosted power.

✅ Your Task:

Write a function called generate_monster_profile(monster).
It should:
Calculate the number of abilities.
Calculate the base power (abilities × 10).
Calculate the boosted power (using elemental boosts).
Return a dictionary like this:
{
    "name": "Goblin",
    "element": "Earth",
    "abilities_count": 2,
    "base_power": 20,
    "boosted_power": 30
}
✅ Bonus:

After generating profiles for all monsters, print them out one by one.

🎯 Hint:

You already have the logic for calculating powers! You can reuse your functions inside this new one!

Here’s your starting list again:

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

def generate_monster_profile(monster):
    profile_dict = {}
    base_power = len(monster['abilities'])*10
    boosted_power = 0
    if monster['element'] == "Earth":
        boosted_power = base_power + 10
    elif monster['element'] == "Fire":
        boosted_power = base_power + 20
    elif monster['element'] == "Water":
        boosted_power = base_power + 30
    profile_dict['name'] = monster['name']
    profile_dict['element'] = monster['element']
    profile_dict['abilities_count'] = len(monster['abilities'])
    profile_dict['base_power'] = base_power
    profile_dict['boosted_power'] = boosted_power
    return profile_dict

for monster in monsters:
    monster_profile = generate_monster_profile(monster)
    print(monster_profile)
'''
