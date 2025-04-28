#Challenge 1 (Simple Battle Simulator)
'''
🧩 Scenario:
Your Monster Lab now hosts *friendly battles* between monsters!

✅ Your Task:
Write a function called battle(monster1, monster2).

The function should:
- Compare the number of abilities each monster has.
- The monster with more abilities wins!

✅ Output:
Print something like:
"{Monster1 Name} wins!" or "{Monster2 Name} wins!" or "It's a tie!"

✅ Example:
- Goblin (2 abilities) vs Dragon (3 abilities) → Dragon wins!
- Slime (3 abilities) vs Dragon (3 abilities) → It's a tie!

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


def battle(monster1, monster2):
    if len(monster1['abilities']) > len(monster2['abilities']):
        print(f"{monster1['name']} wins!")
    elif len(monster2['abilities']) > len(monster1['abilities']):
        print(f"{monster2['name']} wins!")
    else:
        print("It's a tie!")

#Testing
battle(monsters[0], monsters[1])
battle(monsters[1], monsters[2])
battle(monsters[2], monsters[0])
'''

#Challenge 2 (Power Battle Simulator)
'''
🧩 Scenario:
Now let's make battles based on the monsters' **boosted power**
(not just abilities count)!  
Remember: boosted power = (abilities × 10) + elemental bonus.

✅ Your Task:
Write a new function called battle_with_power(monster1, monster2).

The function should:
- Calculate the boosted power for each monster.
- Compare their boosted powers.
- Print the winner (or say "It's a tie!" if powers are equal).

✅ Boosts Reminder:
- Earth → +10
- Fire → +20
- Water → +30

✅ Output:
"{Monster1 Name} wins with {power1} vs {power2}"  
"{Monster2 Name} wins with {power2} vs {power1}"  
or  
"It's a tie! Both have {power}!"

✅ Example:
- Goblin (base 20 + boost 10 = 30)  
- Dragon (base 30 + boost 20 = 50)  
Result → Dragon wins with 50 vs 30!
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

def battle_with_power(monster1, monster2):
    boosted_power1 = len(monster1['abilities'])*10
    boosted_power2 = len(monster2['abilities'])*10
    if monster1['element'] == "Earth":
        boosted_power1 += 10
    elif monster1['element'] == "Fire":
        boosted_power1 += 20
    elif monster1['element'] == "Water":
        boosted_power1 += 30

    if monster2['element'] == "Earth":
        boosted_power2 += 10
    elif monster2['element'] == "Fire":
        boosted_power2 += 20
    elif monster2['element'] == "Water":
        boosted_power2 += 30
    
    if boosted_power1 > boosted_power2:
        print(f"{monster1['name']} wins! with the power: {boosted_power1} vs {boosted_power2}")
    elif boosted_power2 > boosted_power1:
        print(f"{monster2['name']} wins! with the power: {boosted_power1} vs {boosted_power2}")
    elif boosted_power1 == boosted_power2:
        print(f"It's a tie! both have power: {boosted_power1}")

#Testing:
battle_with_power(monsters[0], monsters[1])
battle_with_power(monsters[1], monsters[2])
battle_with_power(monsters[2], monsters[0])
'''

#Challenge 3 (Monster Battle Royale):
'''
🧩 Scenario:
Time for the ultimate battle!
All monsters will battle each other — every monster
fights every other monster!

✅ Your Task:
- Write a function called battle_royale(monsters).
- For each unique monster pair:
    - Have them battle using their boosted power
    (use your battle_with_power function).
- Make sure not to battle the same pair twice!

✅ Output Example:
Goblin vs Dragon → Dragon wins with 50 vs 30  
Goblin vs Slime → Slime wins with 60 vs 30  
Dragon vs Slime → Slime wins with 60 vs 50  

✅ Bonus:
- After all battles, announce the overall strongest
monster by the number of battles they won!
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

# Dictionary to count wins
win_count = {
    "Goblin": 0,
    "Dragon": 0,
    "Slime": 0
}

def battle_with_power(monster1, monster2):
    boosted_power1 = len(monster1['abilities']) * 10
    boosted_power2 = len(monster2['abilities']) * 10
    
    if monster1['element'] == "Earth":
        boosted_power1 += 10
    elif monster1['element'] == "Fire":
        boosted_power1 += 20
    elif monster1['element'] == "Water":
        boosted_power1 += 30

    if monster2['element'] == "Earth":
        boosted_power2 += 10
    elif monster2['element'] == "Fire":
        boosted_power2 += 20
    elif monster2['element'] == "Water":
        boosted_power2 += 30

    if boosted_power1 > boosted_power2:
        print(f"{monster1['name']} wins! with the power: {boosted_power1} vs {boosted_power2}")
        win_count[monster1['name']] += 1
    elif boosted_power2 > boosted_power1:
        print(f"{monster2['name']} wins! with the power: {boosted_power1} vs {boosted_power2}")
        win_count[monster2['name']] += 1
    else:
        print(f"It's a tie! both have power: {boosted_power1}")

def battle_royale(monsters):
    for i in range(len(monsters)):
        for j in range(i+1, len(monsters)):
            battle_with_power(monsters[i], monsters[j])
    
    print("\n Final Results:")
    for name, wins in win_count.items():
        print(f"{name}: {wins} wins")

    # Find overall winner
    overall_winner = max(win_count, key=win_count.get)
    print(f"\n Overall strongest monster: {overall_winner}!")

# Start battle royale
battle_royale(monsters)
'''

#Challenge 4 (Monster Power Ranking):
'''
🧩 Scenario:
You want to **rank** all the monsters based on their boosted power!

✅ Your Task:
- Write a function called rank_monsters(monsters).
- Calculate boosted power for each monster (like before).
- Sort them from highest to lowest boosted power.

✅ Output:
Print something like:
1. Slime (60 power)
2. Dragon (50 power)
3. Goblin (30 power)

✅ Bonus:
Instead of just printing, return a sorted list of monsters
(from highest to lowest power)!

🎯 Example:
If Slime has the highest power, it should be ranked #1!
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

def rank_monsters(monsters):
    for i in range(0, len(monsters)):
        boosted_power = len(monsters[i]['abilities'])*10
        if monsters[i]['element'] == "Earth":
            boosted_power += 10
            monsters[i]['boosted_power'] = boosted_power
        elif monsters[i]['element'] == "Fire":
            boosted_power += 20
            monsters[i]['boosted_power'] = boosted_power
        elif monsters[i]['element'] == "Water":
            boosted_power += 30
            monsters[i]['boosted_power'] = boosted_power
    sorted_monsters = sorted(monsters, key = lambda m: m['boosted_power'], reverse = True)
    for i, monster in enumerate(sorted_monsters, start=1):
        print(f"{i}. {monster['name']} ({monster['boosted_power']} power)")

    return sorted_monsters
sorted_monsters = rank_monsters(monsters)
print(sorted_monsters)
'''
