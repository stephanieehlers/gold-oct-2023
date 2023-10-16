numbers = [1, 2, 3, 4]

#if you need a really long list you can do this

numbers = []
for i in range (1, 101):
    numbers.append(i)
print(numbers)   

# there is a quicker way called list comprehension

numbers = [i for i in range(1, 101)]
print(numbers)

# let's say we want to do this but skip numbers divisible by 3

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)