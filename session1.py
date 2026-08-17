'''
Example 1: My first line of python
'''

#  print('Hello World!');

#Example 2: Printing different things
'''
print('I am learning Python')
print(' My name is Gideon')
print(3.14)
print('Python is', 'great')
'''

# Example 3: Printing a blank line
'''
print('Line one')
print()              #empty print9() blank line
print('Line three')
'''

#Example 4: 
'''
print('Gideon Kiprono')
print('Nairobi')
print()
print('I am read to learn Python')
'''

# Alternative of a new line

# print('Hello\nWorld')


# --------------------------------------------------------------------------
# Creating and Using Variables
#-----------------------------------------------------------------------

# Create varibales
'''
rules: should be lower caps
'''
# name = 'Gideon'
# age = 26
# city = 'Nairobi'

# Using the variables in print()

'''
print(name)
print(age)
print(city)
'''

# Gideon is 26 years old and lives in Nairobi
'''
print(name, "is",age,'years old and lives in', city)
'''

# updating a variable
'''
score= 50

print('Score Before :', score)

score = 75   # Replace the old value

print('score after:',score)

score = score + 10  # Add 10 to the current value

print('Score plus 10:', score)

score = 100

print('Final Score:',score)
'''

# Variable naming rules
'''
case sensitive: age, Age,AGE - different
use snake_case for variables
not use a reserved word e.g class
'''
# student_name = 'Brian'
# phone_number = '0757817127'

# ---------------------------------------------------------------------
# Data Types
# ---------------------------------------------------------------------

# str (string) - text, always in quotes

# name = 'Gideon'

# int (integer) - whole numbers, no quotes

#float - numbers with decimal, no quotes

#bool (boolean) - only two values: True or False

# type() - function that tells you what type a variable is

# print(type(name))


# ---------------------------------------------
# converting between types
# ------------------------------------------------

text_number= '5'
real_number = int(text_number)
print(real_number + 5)

# convert number to  a string

age = 24
age_str = str(age)

print(type(age_str))






