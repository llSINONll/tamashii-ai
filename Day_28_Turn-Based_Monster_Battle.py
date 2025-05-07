#Challenge_1 (Turn-Based Monster Battle)
'''
🧩 Scenario
Your monsters are ready to duel in a full turn-based battle!
We’ll loop the battle until one monster is defeated.

✅ Your Challenge:
Extend your previous Monster, Goblin, and Dragon classes.

Now create a battle system like this:

🧪 Steps to Implement:

while both monsters are alive:
    1. Monster A attacks ➤ deals damage ➤ Monster B takes damage
    2. Check if Monster B is defeated
    3. Monster B attacks ➤ deals damage ➤ Monster A takes damage
    4. Check if Monster A is defeated
📌 Hints:
Create a method like .is_alive() in base class that returns self.hp > 0

You can use time.sleep(1) to slow the fight for drama 😄

Use a while loop and keep the fight going until one monster’s hp <= 0

🧪 Example Output:

Inferno attacks with Flame Breath and deals 24 damage!
Grizzle takes 24 damage. HP is now 76

Grizzle attacks with Club Smash and deals 17 damage!
Inferno takes 17 damage. HP is now 83

...

Inferno has been defeated!
'''

'''
from abc import ABC, abstractmethod
import random
import time

class Monster(ABC):
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.gold = 100
        self.hp = 100

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {amount} damage. HP is now {self.hp}")

    def is_alive(self):
        return self.hp > 0

    
    @abstractmethod
    def attack(self):
        pass

class Goblin(Monster):
    def attack(self):
        damage = random.randint(10,30)
        print(f"{self.name} attacks with Club Smash and deals {damage} damage!")
        return damage

class Dragon(Monster):
    def attack(self):
        damage = random.randint(10,30)
        print(f"{self.name} attacks with Flame Breath and deals {damage} damage!")
        return damage
        
g = Goblin("Grizzle", "Earth")
d = Dragon("Inferno", "Fire")

print("The battle begins!\n")
while g.is_alive() and d.is_alive():
    damage = g.attack()
    d.take_damage(damage)
    if not d.is_alive():
        break
    time.sleep(1)

    damage = d.attack()
    g.take_damage(damage)
    if not g.is_alive():
        break
    time.sleep(1)

if g.is_alive():
    print(f"\n{g.name} wins the battle!")
elif d.is_alive():
    print(f"\n{d.name} wins the battle!")
'''
