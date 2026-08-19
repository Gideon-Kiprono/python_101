# Operators and conditionals: Comparison operators,Logical perators, (if,else if, else), nested if


# Comparison operators
# age = 20
# score = 75

# print(age == 20) #True
# print(age==25)   #False
# print(age!=18)    #True

# print(score>70)    #True
# print(score<50)    #False
# print(score>=75)   #True
# print(score<=74)   #FAlse

# =========================================================
# Basic if statements
# =========================================================

# score = int(input('Enter your score: '))
# if score>= 50:
#     print('You Passed')

#     print('Thank you for taking the score')

# Example if with else(two paths)

"""score = int(input('Enter your score: '))

if score>=50:
    print('Pass - Well done')
else:
    print('Fail - Please ry again')

print(f'Your score was: {score}')
"""
          


# if / elif/ else(many paths)

# score = int(input('Enter score: '))

# if score>=80:
#     print('Grade A - Excellent')
# elif score >= 70:
#     print('Grade B - Good')
# elif score>=60:
#     print('Grace C - Average')
# elif score >=50:
#     print('Grade D - Below average')
# else:
#     print('Grade F - Fail')

#Note: Python stops at the fist True condition . The order matters

# Example of wrong order

# score = int(input('Enter score: '))

# if score>=50:
#     print('Grade D - Below Average')
# elif score >= 70:
#     print('Grade B - Good')
# elif score>=60:
#     print('Grace C - Average')
# elif score >=80:
#     print('Grade A - Pass')
# else:
#     print('Grade F - Fail')


"""print('====Matatu Fare System====')

distance= float(input('Distance in km: '))

if distance <= 5:
    fare=50
    zone= 'Zone 1- CBD'
elif distance <= 15:
    fare = 100
    zone = 'Zone 2 - Suburbs'
elif distance <= 30:
    fare = 150
    zone= 'Zone 3 - Outskirts'
else:
    fare = 250
    zone = 'Zone 4 - Upcountry'

print(f'Zone: {zone}')
print(f'Fare: Ksh {fare}')"""


# score = int(input('Whats your score: '))

# if score>=50:
#     print('Congradulations! You passed.')
# else: 
#     print('Sorry! You did not pass. Try Again.')

# =========================================
# OR operator
# =========================================

# is_student = input('Are you a student? (yes/no): ')
# is_senior = input('Are you 60+? ((yes/no): )')

# if is_student == 'Yes' or is_senior == 'yes':
#     print('Discount applies - 20% off')
# else:
#     print('Full price applies')

# not operator - flips true to false and false to true

is_raining =  False

if not is_raining:
    print('Good day to go for a walk!')
else:
    print('Better stay inside')


