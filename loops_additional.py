"""
additional features with loops
"""
#pass does nothing. This can be used as a filler until you know what you want to put in a code so it doesn't through an error

for i in range(11):
    pass

#nested loops

for a in range (1,6):
    for b in range(1,6):
        print(a, 'x', b, '=', a + b)
#runs the b loop until stops then increases to the next a loop

#Loops with else statements are rarely used in practice

i = 2
while i <5:
    print(i)
    i += 1
else:
    print('else', i)
# else branch is always and only executed once and only once no matter how many times the loop in entered
# exception is when a break statement is entered
#break exits the loop immediately and skips the else