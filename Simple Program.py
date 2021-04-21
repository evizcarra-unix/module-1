"""
Author: Ezra Vizcarra
Topic: Simple Program
Purpose: Nothing too serious with this program. This is to showcase and verify the synchronized process
         with VS Code and GitHub.
"""

#Defined functions for each set {regular, uppercase, lowercase}.
def display_regular(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

#Visual welcome screen to User with a brief intro.
print('----Hello World!----i\nThis is a simple testing sentence formatter:\n'
'   1. Prints regular\n   2. Prints uppercase\n   3.Prints lowercase')

#Skips a line to give it a space between both prints, this requires User to type something.
user_message = input('\nWhat would you like to test? ')

#Calls the functions and prints them as listed on intro in line 21.
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)