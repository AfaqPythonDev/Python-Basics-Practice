'''
List Comprehension
• Create a list of numbers from 1 to 20
• Create a new list of squares using list comprehension
• Print both lists'''


l = list(range(1,21))

sqrl = [i*i for i in l]

print(l)
print(sqrl)




'''
Dictionary Comprehension
• Create a dictionary where keys = numbers 1–5
• Values = cubes of numbers
• Print the dictionary'''

d = {x: x**3 for x in range(1, 6)}

print(d)




'''
join() Practice
• Create a list:
["Python", "is", "awesome"]
• Join into a string
• Print result'''

s = ["Python", "is", "awesome"]

sentence = " ".join(s)

print(sentence)




'''
format() Practice
• Create a string with placeholders
• Insert your name and age using .format()
• Print result'''

a = "My name is {} and my age is {}".format("Afaq", 21)
print(a)





'''
map() Practice
• Create a list:
[1, 2, 3, 4, 5]
• Use map() to square all values
• Print result'''

l = [1, 2, 3, 4, 5]

square = lambda n: n**2

sqrl = map(square, l)

print(list(sqrl))






'''
filter() Practice
• From a list [10, 15, 20, 25, 30]
• Filter only values greater than 20
• Print result'''

l = [10, 15, 20, 25, 30]

greater = lambda a: a > 20 
filtered = filter(greater, l)

print(list(filtered))




'''
reduce() Practice
• From list [1, 2, 3, 4]
• Use reduce() to multiply all values
• Print result'''

from functools import reduce

l = [1, 2, 3, 4]

mult = lambda a,b: a*b
a = reduce(mult,l)

print(a) 





'''
lambda Practice (Intro Only)
• Use lambda to add two numbers
• Print result'''

add = lambda a,b: a+b

print(add(24,35))