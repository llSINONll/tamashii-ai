'''
#Challenge 1(Merge Inventory)
# Character 1 Inventory
inventory_1 = ["Potion", "Elixir", "Sword"]
# Character 2 Inventory
inventory_2 = ["Shield", "Potion", "Bow"]

# 👉 Create a merged inventory list with unique items!
# Output: ['Potion', 'Elixir', 'Sword', 'Shield', 'Bow']
inventory_merged = []
for item in inventory_1:
    inventory_merged += [item]
    
for item_2 in inventory_2:
    if item_2 in inventory_merged:
        continue
    else:
        inventory_merged += [item_2]     
print(inventory_merged)      
'''

'''
#Challenge_2 (Nested Dictionary Stats)
# Expected structure:
# {
#   "name": "Asuna",
#   "stats": {
#     "HP": 120,
#     "MP": 80,
#     "Strength": 15
#   }
# }

# Then print something like:
# Asuna has 120 HP and 80 MP with 15 Strength!

stat = {
   "name": "Asuna",
   "stats": {
     "HP": 120,
     "MP": 80,
     "Strength": 15
   }
 }
stat_2 = stat.get("stats")
print(f"{stat.get('name')} has {stat_2.get('HP')} HP and {stat_2.get('MP')} MP with {stat_2.get('Strength')} Strength!")
'''


'''
#Challenge_3 (List Comprehension for Spells Filtering)
#From a dictionary of spells and MP cost,
#extract all spells that cost less than 40 MP into a list.
spells = {
  "Fireball": 30,
  "Heal": 20,
  "Meteor": 60,
  "Lightning": 35
}

# Use list comprehension to get:
# ["Fireball", "Heal", "Lightning"]

spells_list = []
for s in spells:
    if spells.get(f"{s}") < 40:     #in one line: spells_list = [spell for spell in spells if spells[spell] < 40]
        spells_list += [s]
print(spells_list)
'''
'''
#Challenge_EX(Extra) (Inventory Count Dictionary)
#Turn a list with
#repeated items into a dictionary showing how many of each item you have!
inventory = ["Potion", "Potion", "Elixir", "Sword", "Potion", "Sword"]

# Output:
# {
#   "Potion": 3,
#   "Elixir": 1,
#   "Sword": 2
# }
inventory_dict = {}
count_1 = 0
count_2 = 0
count_3 = 0
for i in inventory:
    if "Potion" == i:
        count_1 += 1
        inventory_dict[i]=count_1
    elif "Elixir" == i:
        count_2 += 1
        inventory_dict[i]=count_2
    elif "Sword" == i:
        count_3 += 1
        inventory_dict[i]=count_3
print(inventory_dict)
'''
'''
#another easy way to do above challenge: 
inventory = ["Potion", "Potion", "Elixir", "Sword", "Potion", "Sword"]
inventory_dict = {}

for item in inventory:
    if item in inventory_dict:
        inventory_dict[item] += 1
    else:
        inventory_dict[item] = 1

print(inventory_dict)
'''
