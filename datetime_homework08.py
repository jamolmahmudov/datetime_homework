#Task 8:
#Write a Python program that subtracts 10 hours from the current time and displays the resulting time.
import datetime
date=datetime.datetime.today()
print(date.hour-10,date.minute)