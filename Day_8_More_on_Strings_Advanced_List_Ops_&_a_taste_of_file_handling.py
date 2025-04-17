'''
#Challenge_1 (Name Formatter)
#Take a user’s full name input like:
#"eugEO"
#And turn it into a properly formatted name:
#"Eugeo"
# Ask user to input full name
name = input("Enter your full name: ")

# Format it properly
formatted_name = name.title()

# Print it
print(f"Welcome, {formatted_name}!")
'''

'''
#Challenge_2 (Remove all Duplicate)
#You're given a list of items — some might be duplicates.
#Create a new list with only unique items (order preserved).

inventory = ["Potion", "Sword", "Potion", "Shield", "Sword", "Bow"]
unique_inventory = []

for item in inventory:
    if item not in unique_inventory:
        unique_inventory.append(item)

print(unique_inventory)
'''

'''
#Challenge_3 (Load Character from a file)
#file reading intro
#Make a file named character.txt with this content:
#Name: Sinon
#Level: 12
#Weapon: Hecate II

#Now write Python code to read this file and print each detail line by line.


with open("character.txt", "r") as read:   #"r" is the read mode
    for text in read:
        print(text.strip()) #strip() removes \n(newline) and extra spaces
        #can also use .read() or .readline() for reading whole file as a string
        #or for reading just a line at a time
'''
'''
# Mini-Boss Challenge (Combo Time!)
#You’re given a list of characters with raw names:

raw_names = ["kiRito", "asUna", "eUgeo", "siNon"]
#✅ Format all names properly (capitalize first letters only)
#✅ Store them into a dictionary with their level (level is index+10)
#✅ Print like: Kirito is at level 10, etc.

f_names = []
dict_names = {}
for index, name in enumerate(raw_names):
    dict_names[name.title()] = index+10
    
for key, value in dict_names.items():
    print(f"{key} is at level {value}")  
'''

'''
#🐉 Secret Boss Challenge: Party Builder - RPG Edition
#You’re given a raw party list of characters
#with messy names and raw stat strings.
#Your mission is to:
#Format each name properly (first letter uppercase only)
#Parse the stats string into an actual dictionary
#Create a final clean dictionary where each character's name maps to their stats dictionary
#Finally, print it in a fancy format like:
#Kirito: HP = 100, MP = 50, Strength = 20


#raw_party = [
#   ["kiRito", "hp:100,mp:50,strength:20"],
#   ["asUna", "hp:90,mp:60,strength:18"],
#   ["euGeo", "hp:95,mp:40,strength:19"]
#]

#Kirito: HP = 100, MP = 50, Strength = 20  
#Asuna: HP = 90, MP = 60, Strength = 18  
#Eugeo: HP = 95, MP = 40, Strength = 19



raw_party = [
   ["kiRito", "hp:100,mp:50,strength:20"],
   ["asUna", "hp:90,mp:60,strength:18"],
   ["euGeo", "hp:95,mp:40,strength:19"]
]

final_party = {}

for lists in raw_party:
    name = lists[0].title()
    stats = lists[1].split(",")
    s = {}
    for stat in stats:
        key, value = stat.split(":")
        s[key.upper()] = value
    final_party[name] = s

print(final_party)
for key, value in final_party.items():
    print(f"{key}: HP = {value.get('HP')}, MP = {value.get('MP')}, Strength = {value.get('STRENGTH')}")
'''
