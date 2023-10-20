"""
Exception Hierarychy
Base exception--> Exception, SystemExit( allows you to close your program manually, Keyboardinterrupt
ArithmeticError-->ZeroDivisionError
LookupError--> IndexError (list is out of range), KeyError (user inputs a name/value not present) 
TypeError: indicates the type of data is not correct with the given context
ValueError: When a value is invalid for some reason (e.g. put a letter when need a nubmer)
"""

#using sys.exit to close a program manually
import sys
user_name = input('What is your name?')
if user_name == '':
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit() # to use this you must import the special import sys 
print('Hello', user_name)
print('Let us get started')


#keyboardinterrupt will stop a program from running endlessly
#Exception: can be used as a template for your own exceptions, for built in exceptions
# you will see the LookUpErrors with lists and dictionaries
#python will try to make the most specific error
