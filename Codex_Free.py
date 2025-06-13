# Variable assignment and manipulation
name = 'Summer Cooke'
user_id = 16180339887
progress = 0.75
xp = 60
verified = True
xp = 80
print(xp)

# Integer
year = 2023
age = 32

#float
pi = 3.14159
meal_cost = 12.99

#String
message = 'good nite'
username = '@snoopdogg'

#boolean - stores a value that can only be either true or false
late_to_class = False
cranky = True

# Operators - arithmetic operators to calculate things
#These include +,-, *, /, and %

score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1

#calculate 20% tip
pizza = 2.99
coke = 0.99

total = pizza + coke
tip= total * 0.2
print (tip)

#another way
tip = (pizza + coke)* 0.2

# Temp in Brooklyn, NY is 86F - Convert to Celsius
temp = 86
celsius = ((temp - 32)/1.8)
print(celsius)

# Exponents using **
score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32

# Calculate BMI in kilo (bmi = mass(kg)/height(m)^2)
mass = 140
masskg = 140* 0.453
heightm = 66 * 0.0254
bmi = masskg/heightm**2
print(bmi)

# Pythagorean Theorem - User Input
username = input ('Enter your name: ')
print(username)

try:
    age = int(input("What is your age? "))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a numeric age.")

#Pythagorean Theorem is the relationship between the three sides of a right triangle
#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.
#Correct formula: c = sqrt(a^2 + b^2), which in Python is: c = (a**2 + b**2)**0.5

a = int(input('What is the length of a? '))
b = int(input('What is the length of b? '))
c = (a**2 + b**2)**0.5
print("The length of the hypotenuse is:", c)

# Currency
#asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))
pesos_usd = 0.00024
soles_usd = 0.28
reais_usd = 0.18
USD = ((pesos * pesos_usd) + (soles * soles_usd) + (reais * reais_usd))
print(f'Your total converted to USD is: {USD} ')

# Coin Flip - Control Flow
#if statements
import random
num = random.randint(0,1) # generates a random number that is either 0 or 1
if num > 0.5:
  print('Heads')
else:
  print('Tails')

# Grades - If Statement
#Check if grade is above or below 55

import random
grade = random.randint(0, 100)
print(f"Your grade is: {grade}")  # So you can see what was generated

if grade >= 55:  # greater than or equal to
    print('You passed')
else:
    print('You have failed')

# Relation Operators
# == equal to, != not equal to, > greater than, < less than
# >= greater than or equal to, <= less than or equal to

# Elif ( multiple else/if)
import random
grade = random.randint(0, 100)
print(f"Your grade is: {grade}")  # So you can see what was generated
if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')

#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.
pH_level = int(input('Enter a pH value (0-14): '))
if pH_level > 7:
  print('Basic')
elif pH_level < 7:
  print('Acidic')
else:
  print('Neutral')

# Magic Eight Ball (Random)
import random
num = random.randint(1,9)
print(num)

# Create Magic Eight Ball
import random

#Ask the user for a question
question = input('What will you ask the Magic 8 Ball? ')

#List of possible answers
answers = [
    'Yes - definitely.',
    'It is decidedly so.',
    'Without a doubt.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

#Select a random answer
magic_8_ball_reply = random.choice(answers)

#Display the result
print(f'You asked: "{question}"')
print(f'The Magic 8 Ball says: {magic_8_ball_reply}')

# Logical Operators (and, or, and not)
#and returns true if both are true, false otherwise
#or returns true if at least one condition is true, false otherwise
#not returns true if the condition is false, vice versa

#Cyclone Exercise:They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits)
# Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variabl

height = int(input('What is your height in cm? '))
credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height >= 137 and credits < 10:
  print('You dont have enough credits')
elif height < 137 and credits >= 10:
  print("you are not tall enough to ride")
else:
  print('you have not met the requirements')


# Sorting Hat
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

Q0 = input("Are you ready to begin the Sorting Hat quiz? (yes or no): ").strip().lower()
#Process the Q0 answer
if Q0 == "yes":
    print("Great! Let the Sorting begin... ")
    # continue to next question...
elif Q0 == "no":
    print("You are kicked out of Hogwarts! ")
    exit()  # Stops the program
else:
    print("Invalid response. Please answer 'yes' or 'no'.")

Q1 = int(input('Do you like Dawn or Dusk? Enter 1 for Dawn and 2 for Dusk '))

#Process the Q1 answer
if Q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif Q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")


print("Q2: When I'm dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
Q2 = int(input("Enter the number of your choice (1–4): "))

#Process Q2
if Q2 == 1:
    hufflepuff += 2
elif Q2 == 2:
    slytherin += 2
elif Q2 == 3:
    ravenclaw += 2
elif Q2 == 4:
    gryffindor += 2   
else:
    print("Wrong input please choose a number 1-4.")

print("Q3: Which kind of instrument most pleases your ear?:")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
Q3 = int(input("Enter the number of your choice (1–4): "))

#Process Q3
if Q3 == 1:
    slytherin += 4
elif Q3 == 2:
    hufflepuff += 4
elif Q3 == 3:
    ravenclaw += 4
elif Q3 == 4:
    gryffindor += 4   
else:
    print("Wrong input please choose a number 1-4.")

print("\nFinal House Scores:")
# Determine the highest scoring house
scores = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

# Get the house(s) with the maximum score
max_score = max(scores.values())
top_houses = [house for house, score in scores.items() if score == max_score]

# Output the result
if len(top_houses) == 1:
    print(f"\n The Sorting Hat has decided... You belong in {top_houses[0]}!")
else:
    print(f"\nIt's a tie between: {', '.join(top_houses)}! The Sorting Hat is confused ")


# Loop - Enter PIN
# loop is also known as repeat, iterate

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

# While Loop
guess = 0
while guess != 6:
  guess = int(input('Guess the number: '))
print('you got it')


# While Loop with tries limit
guess = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')

# Range ()
for i in range(6):
  print(i)

# Print "I will not use Snapchat in class x 100 times"
message = "I will not use Snapchat in class"
for i in range(100):
    print(message)

# Squares
# String concatenation

for i in range(5):
  print('The square of ' + str(i) + ' is ' + str(i*i))

# String interpolation is a process of substituting values of variables into placeholders in a string. 
# For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, nice to meet you!', you would like to replace the placeholder {name} with an actual name. This is string interpolation.

for i in range(5):
  print(f'The square of {i} is {i*i}')

#99 bottles of beers
for i in range(99, 0, -1):
    print(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall")
    print(f"{i} bottle{'s' if i != 1 else ''} of beer")
    print("Take one down, pass it around")
    next_i = i - 1
    if next_i > 0:
        print(f"{next_i} bottle{'s' if next_i != 1 else ''} of beer on the wall\n")
    else:
        print("No more bottles of beer on the wall\n")
# Fizz Buzz
# Program that outputs 1 - 100, with multiples of 3 as Fizz, multiples of 5 as Buzz and For multiples of 3 and 5 as Buzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

git init