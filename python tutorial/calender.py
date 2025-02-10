# Q7. Display the month of calender for a certain year

import calendar
##
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
##
cal = calendar.month(year, month)
print(f'The calender for {month}/{year}:')
print(cal)
