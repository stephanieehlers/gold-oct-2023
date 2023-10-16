#indexing and slicing

fav_band = 'Green Day'
print(fav_band[6])

#if do [:6] that gives the first 5 letters Green

text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)


user_number = input('Please provide a numbers: ')
if user_number.isnumeric():
    print('Thank you, that is a correct number! ')
else:
    print('Sorry', user_number, 'is not a number!')