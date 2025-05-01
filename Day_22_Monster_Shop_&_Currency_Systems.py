#Challenge: Monster Shop with Currency
'''
Scenario:
Each monster earns Gold Coins by winning battles.
They can use this gold to buy special upgrades from the shop.

✅ Your Tasks:
Add a gold field to each monster (start with 100 coins).

Create a shop with available upgrades and their prices:

shop = {
    "Lightning Blade": 40,
    "Ocean Shield": 30,
    "Inferno Cape": 50,
    "Stone Boots": 20
}
Write a function:

def buy_upgrade(monster, upgrade_name)
Which:

Checks if the upgrade is in the shop.

Checks if the monster has enough gold.

Deducts gold and adds the upgrade to the monster.

Prints the result.

💡 Bonus:
Add a battle_reward system where winners of battles
get +20 gold and losers get
+10 gold!
'''
'''
monsters = [
    {
        "name": "Goblin",
        "element": "Earth",
        "abilities": ["Scratch", "Quick Attack"],
        "upgrades": ["Steel Claws", "Earth Armor"],
        "price": 100
    },
    {
        "name": "Dragon",
        "element": "Fire",
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "upgrades": ["Inferno Wings", "Blazing Tail"],
        "price": 100
    },
    {
        "name": "Slime",
        "element": "Water",
        "abilities": ["Bounce", "Split", "Power Strike"],
        "upgrades": ["Mega Bounce", "Tsunami Body"],
        "price": 100
    },
    {
        "name": "Phoenix",
        "element": "Fire",
        "abilities": ["Rebirth", "Flame Wing", "Sky Dive"],
        "upgrades": ["Ash Cloak", "Sun Core"],
        "price": 100
    },
    {
        "name": "Golem",
        "element": "Earth",
        "abilities": ["Stone Fist", "Earthquake"],
        "upgrades": ["Diamond Core", "Stone Skin"],
        "price": 100
    }
]

shop = {
    "Lightning Blade": 40,
    "Ocean Shield": 30,
    "Inferno Cape": 50,
    "Stone Boots": 20
}


def buy_upgrade(monster, upgrade_name):
    if upgrade_name in shop:
        if shop[upgrade_name] <= monster["price"]:
            monster["price"] -= shop[upgrade_name]
            monster["upgrades"].append(upgrade_name)
            print(f"{monster['name']} bought the skill: {upgrade_name} with the price: {shop[upgrade_name]}, remaining gold: {monster['price']}")
        else:
            print(f"{monster['name']} does not have enough gold for {upgrade_name}.")
    else:
        print(f"{upgrade_name} is not available in the shop.")


def boosted_power(monster):
    power = len(monster["abilities"]) * 10  
    if monster["element"] == "Earth":
        power += 10
    elif monster["element"] == "Fire":
        power += 20
    elif monster["element"] == "Water":
        power += 30
    return power


def battle(monster1, monster2):
    power1 = boosted_power(monster1)
    power2 = boosted_power(monster2)

    print(f"{monster1['name']} vs {monster2['name']} - Battle!")

    if power1 > power2:
        print(f"{monster1['name']} wins!")
        monster1["price"] += 20  
        monster2["price"] += 10  
    elif power2 > power1:
        print(f"{monster2['name']} wins!")
        monster2["price"] += 20  
        monster1["price"] += 10 
    else:
        print("It's a tie!")
        monster1["price"] += 15
        monster2["price"] += 15

    print(f"{monster1['name']} has {monster1['price']} gold after the battle.")
    print(f"{monster2['name']} has {monster2['price']} gold after the battle.\n")

battle(monsters[0], monsters[1])  
battle(monsters[2], monsters[3])  

buy_upgrade(monsters[0], "Stone Boots")
buy_upgrade(monsters[1], "Inferno Cape")
'''
#Challenge 2: Monster Tournament Bracket
'''
Scenario:
In this challenge, you’re organizing a monster battle tournament.
Monsters will face off one-on-one, and only the winner advances
to the next round until there’s one final champion left!

Your Tasks:
Pair up monsters for each round.

Determine the winner based on their power and elemental advantages.

Reward the winner with +20 gold and the loser with +10 gold after each battle.

If there’s an odd number of monsters, one monster gets a
free pass to the next round.

Repeat the process until only one monster remains!

Power Calculation:
Abilities: Each ability = +10 power.

Elemental Advantage: Based on the rules you already know:

Water beats Fire.

Fire beats Earth.

Earth beats Water.

Gold Reward:
Winner gets +20 gold.

Loser gets +10 gold.
'''

'''
monsters = [
    {
        "name": "Goblin",
        "element": "Earth",
        "abilities": ["Scratch", "Quick Attack"],
        "upgrades": ["Steel Claws", "Earth Armor"],
        "price": 100  
    },
    {
        "name": "Dragon",
        "element": "Fire",
        "abilities": ["Flame", "Roar", "Ultimate Blast"],
        "upgrades": ["Inferno Wings", "Blazing Tail"],
        "price": 100
    },
    {
        "name": "Slime",
        "element": "Water",
        "abilities": ["Bounce", "Split", "Power Strike"],
        "upgrades": ["Mega Bounce", "Tsunami Body"],
        "price": 100
    },
    {
        "name": "Phoenix",
        "element": "Fire",
        "abilities": ["Rebirth", "Flame Wing", "Sky Dive"],
        "upgrades": ["Ash Cloak", "Sun Core"],
        "price": 100
    },
    {
        "name": "Golem",
        "element": "Earth",
        "abilities": ["Stone Fist", "Earthquake"],
        "upgrades": ["Diamond Core", "Stone Skin"],
        "price": 100
    }
]

def boosted_power(monster):
    power = len(monster["abilities"]) * 10  
    if monster["element"] == "Earth":
        power += 10
    elif monster["element"] == "Fire":
        power += 20
    elif monster["element"] == "Water":
        power += 30
    return power

def elemental_advantage(elem1, elem2):
    if elem1 == "Water" and elem2 == "Fire":
        return True
    elif elem1 == "Fire" and elem2 == "Earth":
        return True
    elif elem1 == "Earth" and elem2 == "Water":
        return True
    return False

def battle(monster1, monster2):
    power1 = boosted_power(monster1)
    power2 = boosted_power(monster2)

    if power1 > power2 or (power1 == power2 and elemental_advantage(monster1["element"], monster2["element"])):
        monster1["price"] += 20  
        monster2["price"] += 10  
        return monster1
    else:
        monster1["price"] += 10  
        monster2["price"] += 20  
        return monster2

def tournament(monsters):
    round_num = 1
    while len(monsters) > 1:
        print(f"\nRound {round_num}:")
        next_round = []
        
        if len(monsters) % 2 == 1:
            free_pass = monsters.pop()
            print(f"{free_pass['name']} gets a free pass to the next round!")
            next_round.append(free_pass)
        
        for i in range(0, len(monsters), 2):
            monster1, monster2 = monsters[i], monsters[i+1]
            print(f"{monster1['name']} vs {monster2['name']}")
            winner = battle(monster1, monster2)
            print(f"Winner: {winner['name']}")
            next_round.append(winner)
        
        monsters = next_round
        round_num += 1
    
    print(f"\nTournament Champion: {monsters[0]['name']}")
    return monsters[0]

tournament(monsters)
'''

