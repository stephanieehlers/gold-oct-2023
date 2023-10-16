cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
cells[0] # output A1, A2, A3
cells[0][0]  # output A1
cells[0][1] # A2
cells[1][2] # B3

#for loop nested list
for x in cells:
    for y in x:
        print('Element:', y)
        
# used to represent multidimentional products like tables
# if you want them to print like a table

'''
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
    
'''

table = [ [i for i in range(1, 6)] for j in range(4) ]
print(table)
