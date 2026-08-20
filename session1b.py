

# acc_type = input('Enter your account type (Basic/Premium): ')
# amount = int(input('Enter amount to send (Ksh): '))

# if acc_type == 'Basic' and amount <= 70000:
#     print('Transaction approved')
# elif acc_type == 'Basic' and amount > 70000:
#     print('Limit exceeded for basic amount (max ksh 70000)')
# elif acc_type == 'Premium' and amount <= 300000:
#     print('Transaction approved')
# elif acc_type == 'Premium' and amount > 300000:
#     print('Limit exceeded for premium account (max ksh 300000)')
# else:
#     print('Unknown account type')

# username = input('Username: ')

# if username == 'admin':
#     password = input('Password: ')
#     if password == 'lux2025':
#         print('Welcome admin')
#     else:
#         print('Incorrect password')
# else:
#     print('User not found')


# Example of nested if

# customer = input('Are you booking HEHA MOVERS? (yes/no): ')
# if customer ==  'Yes':
#     location = input('Where are you moving from?: ')
#     if location == 'Nairobi':
#         print('HEHA MOVERS: Sawa boss, tunakam')
#     else:
#         print('HEHA MOVERS: Boss, hiyo ni safari')
# else:
#     print('HEHA movers: Wrong company boss')



# Example - Nested if vs elif

track = input('Your track(DS or DE): ')

if track == 'DS':
    print('Your next course: PAndas and Numpy')
elif track == 'DE':
    print('Your next course: Airflow and Kafka')
else:
    print('Unknown track')


# Example : Nested if

# has_laptop = input('Do you have a laptop? (yes/no): ')

# if has_laptop == 'yes':
#     os_type = input('Windows or Mac?: ')
#     if os_type == 'Windows':
#         print('Install python from python.org')
#     else:
#         print('python may already be installed - check with python --version')
# else:
#     print('Please borrow a laptop for this session')


