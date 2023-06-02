#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime
x=int(input())
try:
    date=datetime.datetime(year=year , month=2 , day=29)
    print('Mazkur yil kabisa yili')
except:
    print('Bu yil kabisa yili emas')