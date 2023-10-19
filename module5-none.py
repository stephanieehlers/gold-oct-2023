#functions can 1. cause some effect 2. return a meaningful value
#print is a function that doesn't return a meaningful value. just causes an effect
#len doesn't cause effect but does return a value

print('hello')

length = len('Hello')

number = input('What is the number') #this will cause an effect and return a value
print_return = print('hello world')
print(print_return)

x = None

if x:
    print('None is True')
elif x is False:
    print('None is False')
else: 
    print('None is not True, or False, None is just None')
    
x = None
if x is None:   # none is returned as nothing meaningful
    print('yest')
if x == None:
    print('it does')
    
def greet():
    print('hello!')
    
x = greet()
print(x)
    