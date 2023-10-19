"""
dictonary's are created with curly brackets {}
"""

grades = {}    # this creates an empty dictonary
grades['John'] = 'A-' # input for the dictonary is square brackets
grades['Anne'] = 'B'
print(grades)

# if you want to update an entry you can do it in two ways.

grades['Anne'] = 'A'   #just retype the line
print(grades)

#or you can use the following

grades.update({'John':'A'})   #remember to do curly brackets
print(grades)


# len(grades) # gives us the length of the dictonary

if 'John' in grades:
    print('John got:', grades['John'])
    
del grades['John']   #this will delete john
print(grades)

# to iterate a dictionary

grades = {}    # this creates an empty dictonary
grades['John'] = 'A-' # input for the dictonary is square brackets
grades['Anne'] = 'B'
print(grades)

for el in grades:
    print(el)

for el in grades.keys():
    print(el)
    
for el in grades.values(): #prints just the grades
    print(el)
    
for person, grade in grades.items():
    print(person, 'got', grade)