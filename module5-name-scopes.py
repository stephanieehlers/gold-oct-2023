#scope of the name is where the name is recognizable and can be used

def show_truth ():
    mysterious_var = 'Surprise!'
    print(mysterious_var)
show_truth()   

#you can also define the variable outside of the body.so you could move it to after line 6 and it will till work

def show_truth ():
    global mysterious_var   #this means don't use shadowing for mysterious var. Try not to use this. Can be harmful
    mysterious_var = 'New Surprise!' # this is the local variable. this shodows the global variabl
    print(mysterious_var)
    
mysterious_var = 'Surprise!'  # this is the global variable. It is different. This is shadowed by the local variable
print(mysterious_var)
show_truth()  
print(mysterious_var)    # this is called shadowing


def show_truth ():
    mysterious_var.append('New Surprise!')  #if you use square brackets, it will change the outside global variable
    print(mysterious_var)
    
mysterious_var = ['Surprise!']  
print(mysterious_var)
show_truth()  
print(mysterious_var)    