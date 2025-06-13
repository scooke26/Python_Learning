# June 13th - Free Code Camp Day 1
#A variable is a name that references or points to an object.

#Create variable called number and assign 5.
number = 5
shift = 3
print(number)

#Create String
text = "Hello, World!"
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(text)

#String characters can be referenced by numberical index - strings start at 0
#Print the character at index 6
text = "Hello World"
print(text[6])
r = text [6]

# Accessing string from the end , the last has an index of -1
#print last character
print(text[-1])

# Access the number of characters in a string with len() function
# use lens instead of text[-1]
print(len(text))

# get data type of variable
print(type(text)) #string = str
print(type(shift)) #integer = int

# Using .find() position in alphabet of each letter in message
alphabet.find('z')

#Caesar Cipher - find position in alphabet replace with letter 3 after
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = 'Hello World'
alphabet.find(text[0])
print(alphabet.find(text[0]))
#this finds that the first character in text is the 7th in alphabet because a = 0
# if it is not found it returns -1

text = 'Hello World' # uppercase
text = text.lower() # convert to lowercase
print(text.lower()) # just print lowercase
index = alphabet.find(text[0].lower())
print(index)

#Declare a new variable named shifted. Use the bracket notation to access the value of alphabet at index index and assign it to your new variable.
shifted = alphabet[index]
print(shifted)
#reveals letter at index 7 in alphabet which is h
# Find index (7) + shift (3) = 10
shifted = alphabet[index + shift]
print(shifted)

# A loop allows you to repeat a block of code multiple times.
# for loop - Below the line where you declared alphabet, write a for loop to iterate over text. Use i as the loop variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text:
    print(char)  # prints each character in text (indent print for loops)

# Inside the for loop, before printing the current character, declare a variable called index and assign the value returned by alphabet.find(char) to this variable.
for char in text:
    index = alphabet.find(char)
    print(char,index)  # prints the index and char of each character in text.

# Still printing -1 for capitals and spaces lets add this text.lower()
for char in text.lower():
    index = alphabet.find(char)
    print(char, index)

# assign new variable called new_index with the value of index+shift
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    print(char, index, new_index)

#strings are immutable - cannot change them
#we can not change 'brain' to train with string = 'brain' and then string[0] = 't'
#To avoid TypeError - Instead, we can create a new string with the desired changes.

#Delete the text[0] line and reassign text the string 'Albatross'.
text = 'Hello World'
text = 'Albatross'

# add new_char
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]
    print(new_char)  # prints the new character after shifting

# Print new_char and char together
for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new chars:', new_char)

#At the moment, the encrypted character is updated in every iteration. It would be better to store the encrypted string in a new variable. Before your for loop, declare a variable called encrypted_text and assign an empty string ('') to this variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)

#Instead of assigning alphabet[new_index] to encrypted_text, assign the current value of encrypted_text plus alphabet[new_index] to this variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = encrypted_text + alphabet[new_index]
# or encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)
