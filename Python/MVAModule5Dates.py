#The import statement gives us access to the functionality of the datetime class
import datetime
currentDate = (datetime.date.today())
#today is a function that returns today's date
print(currentDate)
print(currentDate.strftime('%d %b, %Y'))