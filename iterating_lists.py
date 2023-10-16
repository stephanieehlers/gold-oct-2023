top_cities = ['NYC', 'LA', 'Chicago', 'Houston']
for city in top_cities: 
    print('Current city:', city)
    
# len returns the number of characters for strings and for lists the number of elements
top_cities = ['NYC', 'LA', 'Chicago', 'Houston']
for city_index in range(len(top_cities)): 
    print('Current city:', city_index, 'Current city:', top_cities[city_index], )

#
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings: 
    sum += spending
print('Money spent: ', sum)
