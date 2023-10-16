#collections or container data types. Can store more than 1 value in a single variable
# 3 types: lists, tuples, dictonaries
# lists: store multiple values of the same type

empty_list = [] 
top_cities = ['New York City', 'LA', 'Chicago']
print(top_cities)
#list indicies start at 0 NOT 1
# indexing provides the number item you want to view
top_cities[0]
# if you do a - in front of the number it reads from the back of the list
#slicing: to get the first few elements
top_cities[0:2] #take the 1st element and stop at the 3rd element. First in inclusive the second is exclusive
top_cities[2:] #means take all elements starting at 2 until the end
top_cities[:3]# take all elements from the start until index of 3
top_cities[:] # means to omit all of them


top_city = 'New York City'
top_cities = []
top_cities[-5] gives you the 6th element from the end