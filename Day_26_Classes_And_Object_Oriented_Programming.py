'''
class keyword is used to define a class followed by the class name..

eg. class Monster:

~
__init__() is a special method that runs automatically
when you create a new object from the class.

self refers to the current object being created.

name and element are the inputs when making a new monster.

Inside __init__, we store those inputs in self.name and self.element,
making them attributes of that specific monster.

eg. def __init__(self, name, element):
        self.name = name
        self.element = element


~
def roar(self):
    print(f"{self.name} the {self.element} monster roars loudly!")

This is a custom method called roar().
It belongs to the Monster class.

When you call it, the monster will print a
roar message using its own name and element.

~
m1 = Monster("Goblin", "Earth")
m2 = Monster("Dragon", "Fire")

Here, you're creating two separate Monster
objects (m1 and m2) using the Monster class.

"Goblin" and "Earth" are passed into
__init__() and assigned to m1.

"Dragon" and "Fire" go to m2.

~
m1.roar()  # Goblin the Earth monster roars loudly!
m2.roar()  # Dragon the Fire monster roars loudly!

You’re telling each object to run its roar() method,
and it uses its own attributes to print a custom message.
'''

'''
Summary:-

✅ class = a blueprint
✅ __init__ = constructor to initialize object data
✅ self.name and self.element = unique data for each object
✅ roar() = a behavior/action that each monster can do
'''

'''
Example:

#Defining the class Monster
class Monster:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def roar(self):
        print(f"{self.name} the {self.element} monster roars loudly!")

#creating the objects
m1 = Monster("Goblin", "Earth")
m2 = Monster("Dragon", "Fire")

#calling the methods inside the class using objects
m1.roar()
m2.roar()
'''

#Challenge_1 (Monster Class with Gold & Abilities)
'''

🔮 Scenario:
You're upgrading your Monster class! Now, each monster should:
Have gold to spend.
Have a list of abilities.
Be able to display its full info.

✅ Your Tasks:
Update the Monster class to include:
gold (start with 100)
abilities (a list of strings)

Create a method:

def display_info(self):
This should print:

Name

Element

Gold

Abilities

🧪 Example:

m1 = Monster("Goblin", "Earth", ["Scratch", "Quick Attack"])
m1.display_info()
✅ Output:

Name: Goblin
Element: Earth
Gold: 100
Abilities: Scratch, Quick Attack
'''

'''
#defining class
class Monster:
    def __init__(self, name, element, abilities):
        self.name = name
        self.element = element
        self.abilities = abilities
        self.gold = 100

    def display_info(self):
        print(f"Name: {self.name}\nElement: {self.element}\nGold: {self.gold}\nAbilities: {", ".join(self.abilities)}")

#creating objects
m1 = Monster("Goblin", "Earth", ["Scratch", "Quick Attack"])
m2 = Monster("Slime", "Water", ["Bounce", "Devour"])

#calling the method using objects
m1.display_info()
print("\n")
m2.display_info()
'''

#Challenge_2 (Spend Gold for an upgrade)

'''
🔮 Scenario:
Now that monsters have gold, let’s give them a
way to spend gold on upgrades (like buying weapons, armor, or magical items).

✅ Your Tasks:
1. Add a method to the Monster class:

def buy_upgrade(self, upgrade_name, cost):
This method should:

Check if the monster has enough gold.

If yes:

Deduct the cost from the monster's gold.

Add the upgrade_name to the monster’s abilities list.

Print a success message.

If no:

Print "Not enough gold to buy <upgrade_name>!"

🧪 Example:

m1 = Monster("Goblin", "Earth", ["Scratch"])
m1.buy_upgrade("Stone Boots", 30)
m1.display_info()

✅ Expected Output:

Goblin bought upgrade: Stone Boots!
Name: Goblin
Element: Earth
Gold: 70
Abilities: Scratch, Stone Boots
'''
'''
class Monster:
    def __init__(self, name, element, abilities):
        self.name = name
        self.element = element
        self.abilities = abilities
        self.gold = 100

    def buy_upgrade(self, upgrade_name, cost):
        if self.gold >= cost:
            self.gold -= cost
            self.abilities.append(upgrade_name)
            print(f"Ability {upgrade_name} Added successfully.")
        else:
            print(f"Not enough gold to buy {upgrade_name}!")
    def display_info(self):
        print(f"Name: {self.name}\nElement: {self.element}\nGold: {self.gold}\nAbilities: {", ".join(self.abilities)}")

m1 = Monster("Goblin", "Earth", ["Scratch"])
m1.buy_upgrade("Stone Boots", 30)
m1.display_info()
'''
