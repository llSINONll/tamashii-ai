'''
✅ What is Inheritance?
Inheritance allows a class (called a child or subclass) to inherit
properties and methods from another class (called a parent or base class).

eg. 
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # from Animal
d.bark()   # from Dog
So Dog inherits from Animal and gets all its methods and
attributes unless overridden.
'''

'''
🔍 What is Abstraction?
Abstraction is one of the core principles of Object-Oriented Programming (OOP).
It involves hiding the complex implementation details of a system and exposing
only the essential features to the user. This simplifies interactions with complex
systems by providing a clear and straightforward interface.

In Python, abstraction is achieved using abstract classes and
abstract methods, which are provided by the abc module.

🧰 Implementing Abstraction in Python
To implement abstraction, you define an abstract
base class using the ABC module and decorate methods
with @abstractmethod. Subclasses then inherit from this
base class and provide concrete implementations of the abstract methods.

🔨 How to Implement Abstraction in Python

from abc import ABC, abstractmethod

class Monster(ABC):  # Abstract base class
    @abstractmethod
    def attack(self):
        pass  # No body here → this must be implemented by child classes

class Goblin(Monster):
    def attack(self):
        print("Goblin attacks with a club!")

class Dragon(Monster):
    def attack(self):
        print("Dragon breathes fire!")

g = Goblin()
g.attack()

d = Dragon()
d.attack()
Monster is abstract and cannot be instantiated.

Both Goblin and Dragon must implement attack() — that's the power
of abstraction: enforcing a contract.
'''

#Challenge_1 (Abstract Monster Blueprint)
'''
🔮 Scenario:
You’re now designing a full Monster System using abstraction!

We’ll define a base abstract class Monster that other monsters
will inherit from. Each monster type will have its own attack() method.

✅ Your Tasks:
Create an abstract class Monster with:

name, element, gold

An abstract method: attack(self)

Create 2 subclasses:

Goblin → attacks with "Club Smash"

Dragon → attacks with "Flame Breath"

Create objects of both and call attack()

🧪 Example Output:

g = Goblin("Grizzle", "Earth")
g.attack()
# Output: Grizzle attacks with Club Smash!

d = Dragon("Inferno", "Fire")
d.attack()
# Output: Inferno attacks with Flame Breath!
'''
'''
from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.gold = 100

    @abstractmethod
    def attack(self):
        pass

class Goblin(Monster):
    def attack(self):
        print(f"{self.name} attacks with Club Smash!!")

class Dragon(Monster):
    def attack(self):
        print(f"{self.name} attacks with the Flame Breath!!")

g = Goblin("Grizzle", "Earth")
g.attack()

d = Dragon("Inferno", "Fire")
d.attack()
'''

#Challenge_2 (Monster Combat System with Random Damage)
'''
🔮 Scenario:
Let’s bring these monsters to life in battle! 
Each monster should now deal random damage when they attack.

✅ Your Tasks:
1. Update the `attack` method in each subclass:

- It should generate a **random damage** value between 10 and 30.
- Print a message including the monster's name, attack type, and the damage dealt.

2. Bonus:
Create a method:
    def take_damage(self, amount):
    - Deducts `amount` from a monster's HP (start all monsters with 100 HP).
    - If HP drops to 0 or below, print: "<name> has been defeated!"

✅ Sample Output:

Grizzle attacks with Club Smash and deals 17 damage!
Inferno attacks with Flame Breath and deals 25 damage!
Grizzle takes 25 damage. HP is now 75.
'''

'''
from abc import ABC, abstractmethod
import random

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


damage = d.attack()
g.take_damage(damage)

damage = g.attack()
d.take_damage(damage)
'''




















