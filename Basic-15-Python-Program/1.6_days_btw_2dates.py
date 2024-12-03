#import datetime module to access date function
from datetime import date 

#given dates first and second respectivly
first_date=date(2024,3,23)
second_date=date(2025,6,12)

#calculating the number of days between 2 dates
no_of_btw=second_date-first_date

#printing the no of days in between
print(f"No of day between {first_date} and {second_date} is {no_of_btw.days}")






