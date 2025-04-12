#Topic 1 input() function and print() (output function)
'''
name = input("Enter your name Adventurer: ")  #use of input() function
print(f"Welcome, {name} to the new world.")

age = int(input("Enter your age: "))
print(f"Your age is: {age}")

print("This is your destiny!!")    #use of print() function

print("Welcome,",name)   #to print multiple variables or strings

#Topic 2 String Manipulation

st = "hello adventurer"
str_up = st.upper()   #we use .upper() to uppercase the string
print(str_up)
'''
'''
st = "HELLO ADVENTURER"
st = st.lower()       #we use .lower() to lowercase the string
print(st)

'''

'''
st = "hello adventurer"
st = st.title()     #we use .title() to only uppercase the first letter of a word
print(st)
name = input("What's your name? ")
print(f"Nice to meet you, {name.title()}!")  # Capitalizes first letter
'''

'''
st = " hello adventurer "
st = st.strip()    #strip or remove the whitespaces 
print(st)
'''

'''
st = "fireball"
st = st.replace("fire","ice")      # .replace(this,from_this) in a string
print(st)
'''

'''
st = "The Blue Rose Sword"
size = len(st)                 #len(string) to find the length of the string
print(size)
'''

'''
st = "Sword"
print(st[0])    #string[index_no.] gives the particular letter in a string in that index no.
'''

'''
st = "Swordmaster"
print(st[0:5])          #[from:to] i'll slice the word from letter at right to:left index no. and exclude the last one
#that's why it gives Sword not Swordm
'''

'''
st = "magic"
print(st[::-1])   #in slicing [start:stop:step] last one is used for step hence staring from -1 means staring from the last letter hence it reverse it
'''

'''
st = "fireball"
print("fire" in st)   #to check if x is in y it'll give True if True
'''

'''
#more parameters in print() function

print("Kirito", "Alice", "Eugeo")  #output: Kirito Alice Eugeo
print("Kirito","Alice","Eugeo", sep="~")   #Output: Kirito~Alice~Eugeo
'''

'''
print("Loading", end="...")   #End the string with the end string...
print(" 100% Completed")
'''

'''
with open("log.txt", "w") as f:
    print("Training Log: Day 3", file=f)   #to redirect the output in a file or to send output in a file
'''

'''
#Challenge_1 (Welcome to the another world)
#Ask the player for their name.
#and print a welcome message using custom sep and end.

name = input("What is your name adventurer: ")
print("Welcome ",name," to the another worldey",sep = "\"", end = ".")
'''

'''
#Challenge_2 (Sword Name Formatter)
#Ask the player to enter their sword name
#in lowercase (e.g., blue rose sword), and:
#Capitalize each word
#Print it in a cool format

sword = input("Enter your sword's name adventurer: ")
print(f"You have the sword: {sword.title()}")
print(f"Is it the great {sword.upper()} really are you serious!!??")
'''
