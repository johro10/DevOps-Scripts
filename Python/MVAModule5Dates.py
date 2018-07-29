# The import statement gives us access to the functionality of the datetime class
import datetime
currentTime = datetime.datetime.now()
#currentDate = (datetime.date.today())
# today is a function that returns today's date
# print(currentDate)
#print(currentDate.strftime('%d %b %Y'))

# challenge
#print(currentDate.strftime("Please attend our event %A, %B %d in the year %Y "))
#userInput = input("What is your birthday? (mm/dd/yyyy)")
# nextBirthday = \
#birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
# difference = nextBirthday + currentDate
# print("Your birth month is " + birthdate.strftime("%B"))
# print(birthday)
# days = currentDate - birthday
# print(days)
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
