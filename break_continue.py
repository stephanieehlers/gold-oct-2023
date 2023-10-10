"""
break and continue instructions
"""
# break instructions are generally used with if statements to close the program

while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
    
# continue is used to escape the current iteration and move on to the next. 
# used with if statements to skip to the nex iteration

for i in range(1, 21): 
    if i % 5 == 0:
        continue
    print(i)
# modulo divided by 5 if 0 then it is divisable by 5   
