'''
#Challenge_1 (Battle Grid Basics)
🧩 Scenario:
You’re building a battle arena where every monster will battle
every other monster once (except themselves, of course).

You want to generate all possible battle pairs and print
them in a readable format.

✅ Your Task:
Loop through all monsters.

For each monster, pair it with every other monster
(no repeats like Goblin vs Goblin).

Print the matchup like this:
"Goblin vs Dragon"
"Goblin vs Slime"
...and so on!

🎯 Sample Output:
Goblin vs Dragon  
Goblin vs Slime  
Dragon vs Goblin  
Dragon vs Slime  
Slime vs Goblin  
Slime vs Dragon  
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

for i in range(len(monsters)):
    for j in range(i+1,len(monsters)):
        print(f"{monsters[i]['name']} vs {monsters[j]['name']}")
        print(f"{monsters[j]['name']} vs {monsters[i]['name']}")
'''
'''
#Challenge_2 (Elemental Strengths)
🧩 Scenario:
In the Monster Battle Arena, each monster has an element (
like Fire, Water, Earth, etc.).
You want to simulate elemental strengths,
where certain elements are stronger than others.
Your task is to print the winner based on the element.

Fire beats Earth.

Earth beats Water.

Water beats Fire.

✅ Your Task:
Loop through all the monsters.

For each pair, compare their elements.

Determine the winner based on the element's strengths.

Print the matchup along with the result like:

"Goblin vs Dragon: Goblin wins!" if Goblin (Earth) beats Dragon (Fire).

"Dragon vs Slime: Slime wins!" if Dragon (Fire) loses to Slime (Water).

🎯 Sample Output:

Goblin vs Dragon: Dragon wins!
Goblin vs Slime: Goblin wins!
Dragon vs Slime: Slime wins!
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
for i in range(len(monsters)):
    for j in range(i+1, len(monsters)):
        if monsters[i]['element'] == "Fire" and monsters[j]['element'] == "Water":
            print(f"{monsters[i]['name']} vs {monsters[j]['name']}: {monsters[j]['name']} wins!")
        if monsters[i]['element'] == "Earth" and monsters[j]['element'] == "Water":
            print(f"{monsters[i]['name']} vs {monsters[j]['name']}: {monsters[i]['name']} wins!")
        if monsters[i]['element'] == "Earth" and monsters[j]['element'] == "Fire":
            print(f"{monsters[i]['name']} vs {monsters[j]['name']}: {monsters[j]['name']} wins!")
'''
