#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))