first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
second = temporary
print('After swapping:', first, second)

#The short cut for the above code is

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

# .sort() sorts the numbers in alphabeticsl or numberical
#.sort(reverse=True) will sort highest to lowest
#print(sorted(list)) this will sort the list but will 
#list_name.sort() sorts the original list
# sorted(list_name) gives back a new, sorted list, keeps the original unchanged
 