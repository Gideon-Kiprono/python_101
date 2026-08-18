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

"""age = 24
age_str = str(age)

print(type(age_str))"""


# ------------------------------------------------------------------------------------
# input() - Talking back to python
# -----------------------------------------------------------------------------------
# Ask the user for their name

# name = input('What is your name? ')
# print('Hello,',name)
# print('Welcome to Python Class')


# age = int(input('How old are you? '))
# print('yYou are,',age,'years old')
# print('Next year you will be', age+1)



# sender = input('Enter Sender name: ')
# recipient = input('Enter recipient name: ')
# amount= int(input('Enter amount to send(ksh): '))
# print()

# print('Sending from',sender,'to',recipient)
# print('Amount:  Ksh ',amount)
# charge = 11
# print('Charge:  Ksh', charge)
# print('Total:  Ksh ',amount + charge)


# buyer_name = input('Enter buyer name: ')
# phone_number = input('Enter phone number: ')
# airtime_amount = int(input('Enter airtime amount (Ksh): '))
# print()
# print('Airtime purchase for', phone_number,'('+buyer_name+')')
# print('Amount: Ksh ',airtime_amount)
# bonus = 5
# print('Bonus: Ksh', bonus)
# print('Total airtime value:  ksh', airtime_amount+bonus)


# -------------------------------------------------------
# f-string - clean way to print
# ----------------------------------------
# f-string basic
name= 'Moses'
age= 29
city= 'Nairobi' 
balance = 15750.50

# Name:, Moses


# f-string way - clean and readable

# print(f'Name: {name} Age: {age} city: {city}')



# f-string with calculation

# price = int(input('Enter price (ksh): '))
# quantity = int(input('Quantity: '))

# subtotal= price *quantity
# vat= subtotal*0.16
# total= subtotal+vat
# print()

# print(f'Item Price: Ksh {price}')
# print(f'Quantity: {quantity}')
# print(f'Subtotal: {subtotal}')
# print(f'VAT: {vat}')
# print(f'TOTAl: {total}')


print('===================================')
print('KENYA SCHOOL GRADE CALCULATOR')
print('===================================')
print()

std_name= input('Student name: ')
subject = input('Subject: ')
print(f'Enter 3 test scores for {std_name}')
test_1= int(input('Test 1: ')) 
test_2= int(input('Test 2: '))
test_3= int(input('Test 3: '))

# Calculate the results
total = test_1 + test_2 + test_3
average= round(total/3,2)
highest=max(test_1,test_2,test_3)
lowest= min(test_1,test_2,test_3)

# Print report
print()
print('======================================')
print(f'REPORT : {std_name}')
print('======================================')
print(f'Subject: {subject}')
print(f'Scores:  {test_1}, {test_2}, {test_3}')
print(f'Total:   {total} / 300')
print(f'Average: {average}')
print(f'Highest: {highest}')
print(f'Lowest:  {lowest}')



