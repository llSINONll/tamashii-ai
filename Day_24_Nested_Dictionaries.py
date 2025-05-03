#Challenge 1: Monster Tech Tree Upgrade System
'''
🧩 Scenario:
Each monster can now upgrade specific abilities with a new "tech tree" system!
Each ability has multiple upgrade levels, and upgrades cost gold.

✅ Your Tasks:
Update the monster structure:
Each monster should have:

-Name

-Element

-Gold

-Abilities with levels (dictionary of ability name → level)

Create a function:
def upgrade_ability(monster, ability_name):
If the ability exists, upgrade it by +1

Cost = 20 gold per level

Deduct gold if affordable, else print "Not enough gold!"

Print upgraded level and remaining gold

Bonus Display Function:
def display_monster(monster):
Show name, element, gold, and list of abilities with current levels.
'''

'''
monster = {
    "name": "Dragon",
    "element": "Fire",
    "gold": 100,
    "abilities": {
        "Flame": 1,
        "Roar": 2,
        "Blast": 1
    }
}

def upgrade_ability(monster, ability_name):
    if ability_name in monster['abilities']:
        if monster['gold'] >=20:
            monster['gold'] -= 20
            monster['abilities'][ability_name] += 1
            print(f"\n{monster['name']} has the upgraded ability: {ability_name} at level {monster['abilities'][ability_name]}. The remaining gold is: {monster['gold']}")
        else:
            print("\nNot enough Gold!")
    else:
        print(f"\nAbility '{ability_name}' not found for {monster['name']}.")
    
upgrade_ability(monster, "Flame")      


def display_monster(monster):
    print(f"\nMonster's Name: {monster['name']}\nMonster's Element: {monster['element']}\nMonster's Gold: {monster['gold']}")
    print("Abilities:")
    for ability, level in monster["abilities"].items():
        print(f"-{ability} at level: {level}")

display_monster(monster)

#Testing:
upgrade_ability(monster, "Flame")

upgrade_ability(monster, "Roar")

upgrade_ability(monster, "Roar")

upgrade_ability(monster, "Roar")

display_monster(monster)
'''

#Challenge 2: Monster Ability Cooldown System
'''
🧩 Scenario:
Now that monsters have powerful abilities,
each ability should have a cooldown –
a number of turns it must wait before being used again.

✅ Your Tasks:
Update monster structure:

Each ability should track both its level and its cooldown counter.

"abilities": {
    "Flame": {"level": 1, "cooldown": 0},
    ...
}
Create a function:

def use_ability(monster, ability_name):
If cooldown is 0:

Print: ability used!

Set cooldown to 3 turns (just an example).

Else:

Print: Ability is on cooldown for X more turns.

Create another function:

def reduce_cooldowns(monster):
Reduce all cooldowns by 1 (to a minimum of 0).

✅ Bonus:
Show a function display_abilities(monster) that prints all abilities with
level and cooldown left.
'''

'''
monster = {
    "name": "Phoenix",
    "element": "Fire",
    "gold": 100,
    "abilities": {
        "Flame Wing": {"level": 1, "cooldown": 0},
        "Sky Dive": {"level": 2, "cooldown": 0}
    }
}

def use_ability(monster, ability_name):
    if ability_name in monster['abilities']:
        if monster['abilities'][ability_name]['cooldown'] == 0:
            print("\nAbility Used!!")
            monster['abilities'][ability_name]['cooldown'] += 3
        else:
            print(f"\nAbility {ability_name} is on the cooldown for {monster['abilities'][ability_name]['cooldown']} more turns.")
    else:
        print(f"\nAbility {ability_name} is not in the monster's ability list.")


def reduce_cooldowns(monster):
    for values in monster['abilities'].values():
        if values['cooldown']>0:
            values['cooldown'] -= 1
        
def display_abilities(monster):
    for abilities, values in monster['abilities'].items():
        print(f"-{abilities} is at level: {values['level']} & with the cooldown: {values['cooldown']}")

#Testing:
use_ability(monster, "Flame Wing")      
use_ability(monster, "Flame Wing")      
reduce_cooldowns(monster)               
use_ability(monster, "Sky Dive")       
reduce_cooldowns(monster)               
reduce_cooldowns(monster)               
use_ability(monster, "Flame Wing")      

display_abilities(monster)        
'''

