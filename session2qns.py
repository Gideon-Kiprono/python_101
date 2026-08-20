# =========================================================
#  QUESTION 1: Age Group Classifier
# =========================================================

"""

Write a program that:
Asks the user for their age (convert to int)
Classifies them into:
o"Child" (0-12)
o"Teenager" (13-19)
o"Adult" (20-64)
o"Senior" (65+)
Prints: "You are a [category].
"""

# print('='*50)
# print('AGE GROUP CLASSIFIER')
# print('='*50)

# age = int(input('Enter your age: '))

# if age <= 12:
#     category = 'Child'
# elif age <= 19:
#     category = 'Teenager'
# elif age <= 64:
#     category = 'Adult'
# else:
#     category = 'Senior'

# print(f'Your are a {category}.')

# print('='*50)

# =========================================================
# QUESTION 2: Even or Odd Checker
# =========================================================

"""

Write a program that:
Asks the user for a number (convert to int)
Checks if the number is even or odd
Prints: "[number] is an even number" or "[number] is an odd number"
Hint: Use the modulo operator % (number % 2 == 0 means even)"""

# print('='*50)
# print('EVEN OR ODD CHECKER')
# print('='*50)

# number = int(input('Enter any number: '))

# if number % 2 == 0:
#     category = 'even'
# else:
#     category ='odd'

# print(f'{number} is an {category} number')

# print('='*50)


# ==========================================================
#  QUESTION 3: Pass/Fail with Subject Details
# ==========================================================


"""Write a program that:
Asks for 3 subject scores (Math, English, Science)
Calculates the average
If average >= 50, prints "PASS"
If average < 50, prints "FAIL"
Also prints the highest score among the 3 subjects"""

# CODE STARTS HERE
# print('='*50)
# print('SUBJECT SCORE ANALYSER')
# print('='*50)

# # input scores
# maths = int(input('Enter math score: '))
# english = int(input('Enter english score: '))
# science = int(input('Enter science score: '))

# # calculate average
# total_score = maths + english + science
# average_score = round(total_score/3,1)

# # Find the highest score
# highest_score = max(maths,english,science)

# # determine best subject
# if maths >= english and maths>=science:
#     best_subject = 'Maths'
# elif english >= maths and english >=science:
#     best_subject = 'English'
# else:
#     best_subject = 'Science'


# print('-'* 50)
# print(f'Average: {average_score}%')

# if average_score >= 50:
#     print('RESULT: PASS')
# else:
#     print('RESULT: FAIL')

# print(f'Best Subject: {best_subject} with {highest_score}%')    

# print('='*50)


# ==========================================================
#  QUESTION 4: Discount Calculator
# ======================================================
"""
Write a program that:
Asks for the total purchase amount (int)
Asks if the user is a member (yes/no)
If member AND amount >= 1000: 20% discount
If member AND amount < 1000: 10% discount
If not member AND amount >= 1000: 5% discount
If not member AND amount < 1000: no discount
Prints the final amount payable with 2 decimal places"""


print("-" * 50)
print('DISCOUNT CALCULATOR')
print("-" * 50)

purchase_amount = int(input('Enter total purchase amount (ksh): '))
member = input('Are you a member? (yes/no): ')

# Determine discount
if member == 'yes' and purchase_amount >= 1000:
    discount_rate = 20
elif member == 'yes' and purchase_amount < 1000:
    discount_rate = 10
elif member == 'no' and purchase_amount >= 1000:
    discount_rate = 5
elif member == 'no' and purchase_amount < 1000:
    discount_rate = 0

# calculte discount
discount = purchase_amount * (discount_rate/100)
final = purchase_amount - discount

print("-" * 50)

print(f'Original Amount: {purchase_amount:.2f}')
print(f'Discount Applied: {discount_rate}% Member Discount')
print(f'Discount Amount: {discount:.2f}')
print(f'Final Amount: ksh {final:.2f}')

print("-" * 50)







# Ask: 'Do you have a bank account? (yes/no): '
# If NO: print 'Sorry, you need an account first.' and stop
# If YES: ask 'How many months have you been a customer? '  (int)
# If less than 6 months: print 'You need at least 6 months of account history.'
# If 6 months or more: ask 'What is your monthly salary? '  (int)
# If salary < 20000: print 'Minimum salary for a loan is Ksh 20,000.'
#If salary >= 20000: print 'Congratulations! You qualify for a loan.'

# has_account = input('Do you have a bank account (yes/no): ')

# if has_account == "yes":
#     month = int(input('How many months have you been a customer?( months): '))
#     if month <= 6 :
#         print('You need at least 6 months of account history.')
#     else:
#         salary = int(input('What is your monthly salary?: '))
#         if salary < 20000:
#             print('Minimum salary for a loan is Ksh 20,000.')
#         elif salary >=20000:
#             print('Congratulations! You qualify for a loan.')

# else:
#     print('Sorry, you need an account first.')









