'''
#Topic 1 Lists - the flexible bag
#It can hold any data type
#Mutable (Changeable) and Ordered

inventory = ["Sword", "Shield", "Potion"]
print(inventory[0])   #Sword
inventory.append("Bow")    #adds bow at the end of the list
inventory[1] = "Magic Shield"   #swap Shield with the Magic Shield
print(inventory)      #prints the inventory in a list

#More methods in the List:

inventory.insert(1,"Elixir")   #it adds the element/item at the desirable index without swapping the one at the same index
print(inventory)

inventory.remove("Bow")    #it removes the element by the value or name
print(inventory)

inventory.pop(3)   #it removes the element by the index
print(inventory)

print(len(inventory))   #it returns the size of the list 


#Topic 2 Tuples - Unchangeable Scrolls

location = ("Forest", 5)
print(location[0])         #we can't do location[0] = "Cave"

player_position = (100, 200)  # (x, y) coordinates
quest = ("Dragon Hunt", True)  # (quest name, is it completed?)
npc = ("Asuna", "Rapier")  # (name, weapon)
'''
'''
#Topic 3 Dictionary - The Labeled Magic Box

stats = {"HP": 100, "MP": 50, "Attack": 12, "Defense": 10}  #key-value pair
print(stats["HP"])   #gives 100 that is the value gives an KeyError if HP doesn't exist
stats["HP"] += 20    #mutable
print(stats["HP"])

#More methods in dictionary:

print(stats.keys())    #gives all of the keys in the dictionary

print(stats.values())   #gives all of the values in the dictionary

print(stats.items())    #gives all of the key-value pairs in the dictionary

print(stats.get("HP"))  #safe way to get values from a key as it'll just return none if key doesn't exist
print(stats.get("Agility", "Unknown"))   #provided the default value if can't find the key
'''

'''
#Challenge_1 (Inventory Manager)
# Create a list called 'inventory' with items like ["Potion", "Elixir", "Sword"]
# Add a new item "Shield" to it
# Remove "Elixir"
# Print your updated inventory


inventory = ["Potion", "Elixir", "Sword"]   #creating an inventory list
inventory.append("Shield")                  #adding the shield to the inventory
inventory.remove("Elixir")                  #it removes the item named elixir
print(inventory)
'''

'''
#Challenge_2 (Stat Booster - Tuple)
# You have a character stat as a tuple: ("Strength", 15)
# Unpack the values into stat_name and value
# Print: "Your <stat_name> is at <value> points!"

stat = ("Strength", 15)
stat_name = stat[0]
value = stat[1]         #we can also do it like stat_name, value = stat
print(f"Your {stat_name} is at {value} points!!")
'''

'''
#Challenge_3 (Character Profile - Dictionary)
# Create a dictionary for a character like:
# {"name": "Kirito", "weapon": "Night Sky Sword", "level": 5}
# Use get() to safely access "level" and "guild"
# If "guild" doesn’t exist, return "Solo Player" as default

char_profile = {"Name": "Eugeo", "Weapon": "Blue Rose Sword", "Level": 10}
print(char_profile.get("Level"))
print(char_profile.get("Guild", "Solo Player"))
'''

'''
#Extra Challenge (List of Dictionary)
# Create a list of dictionaries, each representing a different character
# Example:
# characters = [
#   {"name": "Kirito", "level": 10},
#   {"name": "Asuna", "level": 12}
# ]
# Loop through the list and print: "<name> is at level <level>"


characters = [
  {"name": "Kirito", "level": 10},
  {"name": "Asuna", "level": 12}
]
count = 0
for i in characters:
    print(f"{characters[count].get("name")} is at {characters[count].get("level")}")
    count +=1

#another way to loop through it:
#for character in characters:
#    print(f"{character.get('name')} is at level {character.get('level')}")
'''
