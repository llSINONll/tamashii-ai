'''
🧠 What is Multiple Inheritance?
In Python, a class can inherit from more than one parent class.
This allows the child class to access attributes and methods of
all its parents.

🔹 Syntax:

class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # From Parent1
c.method2()  # From Parent2
🔁 What if both parents have the same method?
Python follows the Method Resolution Order (MRO) — it looks
for the method from left to right in the class definition.

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):  # A comes first
    pass

c = C()
c.greet()  # Output: Hello from A
#Use ClassName.__mro__ or help(ClassName) to see the full MRO.
print(A.__mro__)
'''


#Challenge_1 (Monster+Trader = Hybrid!)
'''
🔮 Scenario:
We want to create a monster that can not only battle,
but also trade items using multiple inheritance.

✅ Your Tasks:
1. Create two base classes:

   - `Monster`: with name, element, and attack()
   - `Trader`: with inventory (list of items) and method show_inventory()

2. Create a subclass `MerchantMonster` that inherits from both.

3. Create an object of MerchantMonster and:
   - Call `attack()`
   - Call `show_inventory()`

🧪 Example Output:
Grizzle attacks with Club Smash!
Inventory: ['Potion', 'Elixir', 'Scroll']
'''
'''
class Monster:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def attack(self):
        print(f"{self.name} attacks with Club Smash!")

class Trader:
    def __init__(self):
        self.inventory = ['Potion', 'Elixir', 'Scroll']

    def show_inventory(self):
        print(f"Inventory: {self.inventory}")

class MerchantMonster(Monster, Trader):
    def __init__(self, name, element):
        Monster.__init__(self, name, element)
        Trader.__init__(self)

# Test
m = MerchantMonster("Grizzle", "Earth")
m.attack()
m.show_inventory()
'''

#Challenge_2 (Polymorphic Monster Army)

'''
🧩 Scenario:
Let’s bring polymorphism to action!
You now have an army of different monster types, and each
should attack differently using a common interface.

✅ Your Tasks:
Create a list of Monster objects, some Goblins and some Dragons.

Loop through this list and call .attack() on each monster.

Thanks to polymorphism, each monster will use its own attack method,
even though the loop is generic.

🧪 Sample Output:
Grizzle attacks with Club Smash and deals 14 damage!
Inferno attacks with Flame Breath and deals 28 damage!
Goblo attacks with Club Smash and deals 22 damage!
Smaug attacks with Flame Breath and deals 19 damage!
✅ Your Starting Code:

from abc import ABC, abstractmethod
import random

class Monster(ABC):
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.gold = 100
        self.hp = 100

    @abstractmethod
    def attack(self):
        pass

class Goblin(Monster):
    def attack(self):
        damage = random.randint(10, 30)
        print(f"{self.name} attacks with Club Smash and deals {damage} damage!")

class Dragon(Monster):
    def attack(self):
        damage = random.randint(10, 30)
        print(f"{self.name} attacks with Flame Breath and deals {damage} damage!")

# Monster army
army = [
    Goblin("Grizzle", "Earth"),
    Dragon("Inferno", "Fire"),
    Goblin("Goblo", "Earth"),
    Dragon("Smaug", "Fire")
]

# Polymorphic attacks
for monster in army:
    monster.attack()
