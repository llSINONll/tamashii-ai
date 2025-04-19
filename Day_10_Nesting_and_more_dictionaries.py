'''
#Challenge_1 (Challenge Skill Tracker)
#You’re given a list of dictionaries, where each dictionary contains a character name and a list of their skills.
#party = [
#  {"name": "Kirito", "skills": ["Dual Blades", "Sword Rain", "Starburst Stream"]},
#  {"name": "Asuna", "skills": ["Rapier", "Heal", "Mother's Rosario"]},
#  {"name": "Sinon", "skills": ["Sniping", "Hecate II", "Stealth Shot"]}
#]
#✅ Your Task:
#Loop through the list and print:
#Kirito knows: Dual Blades, Sword Rain, Starburst Stream  
#Asuna knows: Rapier, Heal, Mother's Rosario  
#Sinon knows: Sniping, Hecate II, Stealth Shot

party = [
  {"name": "Kirito", "skills": ["Dual Blades", "Sword Rain", "Starburst Stream"]},
  {"name": "Asuna", "skills": ["Rapier", "Heal", "Mother's Rosario"]},
  {"name": "Sinon", "skills": ["Sniping", "Hecate II", "Stealth Shot"]}
]

for name in party:
    n = name["name"]
    list_skill = name["skills"]
    print(f"{n} knows: {', '.join(list_skill)}")
'''
'''
#Challenge_2 (Skill Display Mastery)
#You’re given a party of characters (same as before), and each character has a list of skills.
#party = [
#  {"name": "Kirito", "skills": ["Dual Blades", "Sword Rain", "Starburst Stream"]},
#  {"name": "Asuna", "skills": ["Rapier", "Heal", "Mother's Rosario"]},
#  {"name": "Sinon", "skills": ["Sniping", "Hecate II", "Stealth Shot"]}
#]
#✅ Your Task:
#Loop through the party and print each character's
#name with their skills as a clean comma-separated string like:
#Kirito: Dual Blades, Sword Rain, Starburst Stream  
#Asuna: Rapier, Heal, Mother's Rosario  
#Sinon: Sniping, Hecate II, Stealth Shot


party = [
  {"name": "Kirito", "skills": ["Dual Blades", "Sword Rain", "Starburst Stream"]},
  {"name": "Asuna", "skills": ["Rapier", "Heal", "Mother's Rosario"]},
  {"name": "Sinon", "skills": ["Sniping", "Hecate II", "Stealth Shot"]}
]

for member in party:
    name = member["name"]
    skills = member["skills"]
    print(f"{name}: {', '.join(skills)}")
'''

'''
#Final Challenge (Ultimate Skill Viewer)
#You're given an RPG party. Each member has a name and a list of skills.
#Each skill is a dictionary with a name and a power level.
#party = [
#    {"name": "Kirito", "skills": [{"name": "Dual Blades", "power": 90}, {"name": "Starburst Stream", "power": 100}]},
#    {"name": "Asuna", "skills": [{"name": "Heal", "power": 60}, {"name": "Mother's Rosario", "power": 95}]},
#    {"name": "Sinon", "skills": [{"name": "Sniping", "power": 85}, {"name": "Stealth Shot", "power": 80}]}
#]
#✅ Your Task:
#Loop through the party and for each character, print all their skill names
#and power levels like:
#Kirito's Skills:
#- Dual Blades (Power: 90)
#- Starburst Stream (Power: 100)

#Asuna's Skills:
#- Heal (Power: 60)
#- Mother's Rosario (Power: 95)

#Sinon’s Skills:
#- Sniping (Power: 85)
#- Stealth Shot (Power: 80)


party = [
    {"name": "Kirito", "skills": [{"name": "Dual Blades", "power": 90}, {"name": "Starburst Stream", "power": 100}]},
    {"name": "Asuna", "skills": [{"name": "Heal", "power": 60}, {"name": "Mother's Rosario", "power": 95}]},
    {"name": "Sinon", "skills": [{"name": "Sniping", "power": 85}, {"name": "Stealth Shot", "power": 80}]}
]

for member in party:
    name = member["name"]
    skills = member["skills"]
    print(f"{name}'s Skills:")
    for skill in skills:
        print(f"- {skill['name']} (Power: {skill['power']})")
    print("-" * 30)
'''
