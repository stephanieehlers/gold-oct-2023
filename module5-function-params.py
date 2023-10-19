


def get_average(input_numbers): # input_numbers is a parameter. and must be listed to make this function work. 
    sum = 0.0
    for number in input_numbers:
     sum += number
    average = sum / len(input_numbers) # assign a value to a paramter when we invoke a function
    print(average)
    
get_average([5.0, 3.5, 7.8, 9.9, 10.0])    #[] this is called an argument. The value of the argument is assigned to the parameter input_numbers

#when you invoke a function you must provide all of the arguments

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)    
    
print_letter_count('Welcome', 'e')
    
    #positional arguments
print_letter_count(letter='e'):   
    
    