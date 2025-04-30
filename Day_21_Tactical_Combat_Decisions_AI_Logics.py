#Challenge 1: Elemental Counter Logic
'''
Scenario: Monsters should decide whether to fight, flee, or fuse
based on elemental advantage and power level.

✅ Your Task:
Write a function tactical_decision(monster1, monster2) that:

Calculates their boosted powers (as before).

Uses the element matchup rules:

Water beats Fire

Fire beats Earth

Earth beats Water

If monster1 has higher power and a winning element → Fight

If monster1 has lower power and losing element → Flee

Else → Fuse

🔍 Example Output:
Dragon vs Slime → Decision: Flee
Goblin vs Slime → Decision: Fuse
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

def get_elemental_advantage(elem1, elem2):
    return (elem1 == "Water" and elem2 == "Fire") or \
           (elem1 == "Fire" and elem2 == "Earth") or \
           (elem1 == "Earth" and elem2 == "Water")

def get_boosted_power(monster):
    power = len(monster['abilities']) * 10
    if monster['element'] == "Earth":
        power += 10
    elif monster['element'] == "Fire":
        power += 20
    elif monster['element'] == "Water":
        power += 30
    return power

def tactical_decision(monster1, monster2):
    power1 = get_boosted_power(monster1)
    power2 = get_boosted_power(monster2)

    wins = get_elemental_advantage(monster1['element'], monster2['element'])
    loses = get_elemental_advantage(monster2['element'], monster1['element'])

    if power1 > power2 and wins:
        decision = "Fight"
    elif power1 < power2 and loses:
        decision = "Flee"
    else:
        decision = "Fuse"

    print(f"{monster1['name']} vs {monster2['name']} => Decision: {decision}")
    return decision

tactical_decision(monsters[1], monsters[2]) 
tactical_decision(monsters[0], monsters[2])  
'''

#Challenge 2: Monster Tournament Bracket
'''
🧩 Scenario:
You’re organizing a monster battle tournament!
Monsters will face off one-on-one,
and only the winner advances to the next round until
one final champion remains!

✅ Your Task:
Create a function tournament_winner(monster_list)

For each round:

Pair up monsters

Use boosted power + elemental advantage to determine the winner

If an odd number of monsters, one gets a free pass to the next round

Continue until only one winner remains.

🧠 Power Rules (same as before):
Each ability = +10 power

Earth: +10

Fire: +20

Water: +30

Elemental advantage gives +15 bonus power
(you can reuse the get_elemental_advantage function from before!)

🎯 Example Output:
Round 1:
- Goblin vs Dragon → Winner: Dragon
- Slime gets a free pass

Round 2:
- Dragon vs Slime → Winner: Slime

👑 Tournament Champion: Slime
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
    },
    {
        "name": "Phoenix",
        "element": "Fire",
        "abilities": ["Rebirth", "Flame Wing", "Sky Dive"],
        "upgrades": ["Ash Cloak", "Sun Core"]
    },
    {
        "name": "Golem",
        "element": "Earth",
        "abilities": ["Stone Fist", "Earthquake"],
        "upgrades": ["Diamond Core", "Stone Skin"]
    }
]
def elemental_advantage(elem1, elem2):
    return elem1 == "Water" and elem2 == "Fire" or \
           elem1 == "Fire" and elem2 == "Earth" or \
           elem1 == "Earth" and elem2 == "Water"

def boosted_power(monster):
    power = len(monster["abilities"])*10
    if monster["element"] == "Earth":
        power += 10
    elif monster["element"] == "Fire":
        power += 20
    elif monster["element"] == "Water":
        power += 30
    return power

def battle(mon1, mon2):
    power1 = boosted_power(mon1)
    power2 = boosted_power(mon2)

    if elemental_advantage(mon1["element"], mon2["element"]):
        power1 += 15
    elif elemental_advantage(mon2["element"], mon1["element"]):
        power2 += 15

    return mon1 if power1 >= power2 else mon2


def tournament_winner(monsters):
    round_num = 1
    while len(monsters) > 1:
        print(f"\nRound {round_num}:")
        next_round = []
        i = 0
        while i < len(monsters):
            if i + 1 < len(monsters):
                mon1 = monsters[i]
                mon2 = monsters[i + 1]
                winner = battle(mon1, mon2)
                print(f"{mon1['name']} vs {mon2['name']} => Winner: {winner['name']}")
                next_round.append(winner)
                i += 2
            else:
                print(f"{monsters[i]['name']} gets a free pass")
                next_round.append(monsters[i])
                i += 1
        monsters = next_round
        round_num += 1

    print(f"\nTournament Champion: {monsters[0]['name']}")
    return monsters[0]

tournament_winner(monsters)    
''' 
