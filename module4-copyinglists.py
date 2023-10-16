name_original = 'Jon Snow'
name_new = name_original #These will copy the same lists. but if you want to define it differently you need to use slicing


list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# to get these lists to print as we want, we need to use slicing
list_original = [1, 2, 3]
list_new = list_original [:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

