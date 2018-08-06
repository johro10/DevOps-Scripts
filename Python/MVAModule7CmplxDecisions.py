# Declare initial variable value
depositAmount = 0

# deposited amount
depositAmount = int(input('How much are you depositing today? '))

# Branching statements
if depositAmount > 100 and depositAmount <= 1000:
    print('Enjoy your free toaster!')
elif depositAmount > 1000 and depositAmount <= 2500:
    print('Enjoy your free TV!')
elif depositAmount > 2500 and depositAmount <= 5000:
    print('Enjoy your free Motorcycle!')
elif depositAmount > 5000:
    print('Enjoy your new car!')
else :
    print('Thanks for visiting our bank!')
print('Have a nice day! ')
