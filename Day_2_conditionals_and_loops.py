'''#Topic 1 if-elif-else conditional statements

hp = 50
if(hp>70):
    print(f"You're Strong your hp is: {hp}")
elif(hp>30):
    print(f"You're injured your hp is: {hp}")
else:
    print(f"You're Critical your hp is: {hp}")
'''

'''
#Topic 2 for loop

inventory = ["Blue Rose Sword", "Potion", "Elixir"]

for item in inventory:
    print(f"You have item: {item}")
'''
'''
#Topiic 3 while loop

stamina = 3
while stamina > 0:
    print("Swing Sword!!")
    stamina -= 1
'''
'''
#break and continue in for loop

for i in range(5):   #range is from 0 to 4
    if i == 2:
        continue    #to skip this iteration
    if i == 4:
        break       #to break the loop
    print(i)
'''
'''
#Mini Challenge_1 of today:

#1. Eugeo swings sword 5 times.
#2. After 3 swings, he gets tired
#3. Use a for loop
#4. Print "Swing", then "Eugeo is tired.... after 3rd swing"


for i in range(1,6):
    print("Swing!!")

    if(i == 3):
        print("Eugeo is tired after 3rd swing...")
        
'''
'''
#Mini challenge_2 (Potion Identifier):

#If you have a potion, check its color and decide its effect:
#- "Red" = Heals HP
#- "Blue" = Restores MP
#- "Green" = Boosts Defense
#If it's anything else, print "Unknown Potion!"

inventory_potion = ["Red", "Blue", "Yellow", "Light Blue", "Green", "Golden"]

for color in inventory_potion:
    print(f"\nColor of the potion: {color}")
    if color == "Red":
        print("Potion's effect: Heals HP")
    elif color == "Blue":
        print("Potion's effect: Restores MP")
    elif color == "Green":
        print("Potion's effect: Boosts Defense")
    else:
        print("Unknown Potion!!")
'''
'''
#Mini Challenge_3 (Inventory Scanner):

#Loop through a character’s inventory and:
#- If the item is "Potion", print "Heal Ready!"
#- If "Elixir", print "MP Restore Ready!"
#- Else, just print the item name.

inventory = ["Blue Rose Sword", "Potion", "Elixir", "Fishing Rod", "Town's Map"]

for item in inventory:
    if item == "Potion":
        print("Heal Ready!")
    elif item == "Elixir":
        print("MP Restored Ready!!")
    else:
        print(f"You have the item: {item}")
'''
'''
#Mini Challenge_4 (Dungeon Escape):

#You have 5 steps to escape.
#Each time you walk, decrease the steps.
#But if you're at step 3, a monster appears → Print "Monster Encounter!"
#Stop at step 0 → Print "Escaped!"

step = 5
while step >= 0:
    if(step == 3):
        print(f"Monster Encounter!! at Step {step}")
    if (step == 0):
        print(f"Escaped!! at Step {step}")
    step -= 1
'''
'''
#Mini Challenge_5 (Training Grounds)

#Kirito wants to train by attacking a dummy 10 times.
#- Every 2 attacks, print "Combo x2!"
#- If attack number is 7, break and print "Kirito got tired!"

attack = 10

for hit in range (1,attack+1):
    if hit == 7:
        print("Kirito got tired!")
        break
    if hit%2 != 0:
        continue
    else:
        print("Combo x2")
'''
'''
#Mini Challenge_6 (Unlock the Door):

#User has 3 chances to enter a password.
#If password is correct (e.g. “Aincrad123”), print “Access Granted”.
#Else, print “Wrong Password”.
#After 3 failed tries, print “Locked Out!”

count = 1
while True:
    p = input("Enter the password to Aincrad: ")
    if(p == "Aincrad123"):
        print("Access Granted!!")
        break
    elif count == 3:
        print("Locked Out!!")
        print(f"Attempt {count} out of 3")
        break
    else:
        print("Wrong Password")
    print(f"Attempt {count} out of 3")
    count+=1
'''
'''
#Mini Challenge_7 (Stat Analyzer):
#Check a character's stats:
#- If Attack > 10 and Agility > 10 → “Speed Slayer”
#- If Defense > 10 and Magic > 20 → “Mystic Tank”
#- Else → “Balanced Type”


stats_1 = {"Attack": 11, "Defense": 7, "Agility": 12, "Magic": 15}

# Step 1: Print stats
for stat, value in stats_1.items():
    print(f"{stat}: {value}")

# Step 2: Analyze using conditions
if stats_1["Attack"] > 10 and stats_1["Agility"] > 10:
    print("Speed Slayer")
elif stats_1["Defense"] > 10 and stats_1["Magic"] > 20:
    print("Mystic Tank")
else:
    print("Balanced Type")
'''
'''
#Mini challenge_8 (Respawn Loop)
#Player HP starts at 0. Keep asking "Do you want to respawn? (yes/no)"
#- If yes, set HP to 100 and print "Respawned!"
#- If no, print "Game Over" and end.

hp = 0
while hp==0:
    res = input("Do you want to respawn? (yes/no): ")
    if res.lower() == "yes":
        print("Your HP is set to 100")
        print("Respawned!!")
        hp+=100
        print(f"Your HP is now: {hp}")
        break
    elif res.lower() == "no":
        print("Game Over!!")
        break
    else:
        print("Invalid Choice please Enter right Choice!!")
'''
