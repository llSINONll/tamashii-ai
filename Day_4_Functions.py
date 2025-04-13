'''
#Function definition and calling

def greet():     #function definition
    print("Welcome, Adventurer to the new world")     #function body

greet()       #function calling
'''

'''
#Function parameters

def greet_player(name):     #name is a parameter
    print(f"Welcome, {name} to the new world")

greet_player("Eugeo")     #function calling by passing an argument
'''

'''
#Returning values in a function

def stats(atk,defe,agi):
    return atk+defe+agi

total_s = stats(10,9,12)
print(f"Your total stats sum is: {total_s}")
'''

'''
#default parameters in a function

def heal(name = "Adventurer"):
    print(f"{name} heals 50 HP!!")

heal()      #it will use default value
heal("Eugeo")   #This argument overrides default value
'''

'''
#Funtions with Input
def ask_name():
    name = input("Ente your name adventurer: ")
    print(f"Welcome, {name} to the new world!!")

ask_name()
'''

'''
#Challenge_1 (HP Potion)
#Create a function called restore_hp that takes one parameter 'name'
# It should print: "<name> used a potion and restored 50 HP!"
# Call the function with your name or any character name
# Extra XP: Add a second optional parameter for amount (default = 50)


def restore_hp(name = "Adventurer", hp = 50):
    print(f"{name} used a potion and restored {hp} HP!!")

restore_hp()           #for both default values
restore_hp("Kirito")     #for default value of hp
restore_hp("Eugeo",60)   #for give values
'''

'''
#Challenge_2 (Battle Damage Calculator)
# Create a function called calculate_damage that takes two parameters:
# attack_power and defense_power
# The formula = attack_power - defense_power
# Return the final damage and print: "You dealt <damage> damage!"

# Call it with some sample values like: (100, 40)
#Extra XP: If damage is less than 0, make it 0
#(because negative damage makes no sense lol)

def calculate_damage(attack_power, defense_power):
    dmg = attack_power - defense_power
    if(dmg <= 0):
        dmg = 0
    print(f"You dealt {dmg} damage!!")
    return dmg

calculate_damage(100,40)
calculate_damage(100,140)
'''

'''
#Challenge_3 (Mana Usage Tracker)
#Create a function called cast_spell that takes two parameters:

#spell_name (like "Fireball")
#mp_cost (like 30)

#It should print:
#️"<spell_name> was cast! It used <mp_cost> MP!"

#Extra XP:
#If mp_cost > 50, print an extra line →
#"That was a powerful spell!"


def cast_spell(s_name, mp_cost):
    print(f"{s_name} was cast! It used {mp_cost} MP!!")
    if(mp_cost>50):
        print("That was a powerful spell!!")

cast_spell("Fireball", 30)
cast_spell("Explosion!!!", 100)
'''

'''
#Challenge_4(Stat Booster)
#Write a function called boost_stat with:
#stat_name (like "Strength")
#amount (like 10)
#It should print:
#"Your <stat_name> increased by <amount> points!"

#Extra XP:
#Make the function have a default amount of 5,
#in case the player didn’t mention it.

def boost_stat(stat_name, amount=5):
    print(f"Your {stat_name} increased by {amount} points!!")
boost_stat("Attack")
boost_stat("Agility", 10)
'''


#🏆 Final Challenge (Character Creator)
#You’re building your own RPG character setup screen!

#🔧 Instructions:
#Create a function called create_character that takes:
#name → The name of the character
#weapon → The weapon name
#hp (default = 100)
#mp (default = 50)
#Inside the function:
#Capitalize the name and weapon properly.
#Print out something like this:

#🌟 Character Created! 🌟
#Name: Kirito
#Weapon: Blue Rose Sword
#HP: 100 | MP: 50
#Ready for adventure!
#🔁 Call the function with:
#create_character("kirito", "blue rose sword")
#create_character("asuna", "rapier", 120, 80)


def create_character(name = "Traveler", weapon = "Wooden Sword", hp = 100, mp = 50):
    name = name.title()
    weapon = weapon.title()
    print(f"\n🌟 Character Created! 🌟 \nName: {name}\nWeapon: {weapon}\nHP: {hp} | MP: {mp}\nReady for Adventure!!")

create_character()   #all default o/p
create_character("Eugeo", "Blue Rose Sword")   #given only name and weapon name
create_character("Kirito", "Black Tree Sword",999,999)   #given all things
    
    
