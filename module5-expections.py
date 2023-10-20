"""
Erros
"""
#syntax errors: mean you made a mistake in the code
#Value Error: Program is correct but the user entered something that isn't correct
#to handle exceptions when a user enters the wrong thing you can add code to navigate that

try: # try and except will help to prevent those value error/exception errors
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except: # this is where we handle what happens if an exception error occurs
    print('You did not provide a number, so i will not calculate the inverse!')
    
 #for the above code if you put a zero in it will print the except message. 
 #The error is called a zeroDivisionError. We could expand out try except to cover both errors
 
 try: # try and except will help to prevent those value error/exception errors
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError: #specify the error branches
    print('You did not provide a number, so i will not calculate the inverse!') 
except ZeroDivisionError:
    print('You provided a 0 and division by 0 is not possible, sorry')
    
    
 try: # try and except will help to prevent those value error/exception errors
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError: #specify the error branches
    print('You did not provide a number, so i will not calculate the inverse!') 
except ZeroDivisionError:
    print('You provided a 0 and division by 0 is not possible, sorry')  
except: #a general except to capture anything else
    print('Something strange happened here, sorry')
    
    
    """
    If you raise a SyntaxError manually, then you can catch it in the except block just fine:

try:
  raise SyntaxError
except:
  print('Got it!') # SyntaxError is caught here
However, if you make a syntax error in the try block and Python automatically raises a SyntaxError for you, then you cannot catch it:

try:
  5:4 # this line generates a SyntaxError
except:
  print('Got it!') # SyntaxError is NOT caught here
  
"""    
    