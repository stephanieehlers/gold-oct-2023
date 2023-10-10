"""
for loops
"""
# used to go through specific elements in a sequence of events. Scan all elements

for letter in 'hello!':  
    print('Current letter:', letter)
    # python knows when the sequence needs to end. For this example it will end after it 
    # scans each character. It scans by iterations

for counter in range (1, 11): 
    print(counter)
print('Finished')  
#range shows the range to run through. 1 is the start and 11 is the stop value
#Stop value is included but is not listed. You won't see 11. It will actually stop at 10
# if no start ID then will start at 0
# if list as range(1, 11, 2) it will generate every second number

for counter in range (1, 11, 2): 
    print(counter)
print('Finished')  