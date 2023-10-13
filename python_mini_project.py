import random
import string

instances = int(input('How many EC2 instances would you like names for? '))
department = input('What Department are you in? ')
n = instances




if department == 'Marketing' or department == 'Accounting' or department == 'FinOps' :
    print('Here are your unique instance names : ')
    
    for z in range(0, n) : 
    # get random string of letters and digits
        name = string.ascii_letters + string.digits
        instance_name = ''.join((random.choice(name) for i in range(8)))     
    
        print(random.randrange(1,100), instance_name)
else :        
    print('Sorry, your Department does not use this name generator ') 

    
   