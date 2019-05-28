"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input = input('type month and year ')

li = user_input.split(' ')

date = datetime.now().strftime('%Y-%m')
dateli = date.split('-')
curcal = calendar.TextCalendar()

if len(li) == 1 and len(li[0]) == 0:
  print(curcal.formatmonth(int(dateli[0]), int(dateli[1]) ))
elif len(li) == 1 and len(li[0]) > 0:
  print(curcal.formatmonth(int(dateli[0]), int(user_input[0]) ))
elif len(li) == 2:
  print(curcal.formatmonth(int(li[1]), int(li[0]) ))
else:
  print('Wrong format')
