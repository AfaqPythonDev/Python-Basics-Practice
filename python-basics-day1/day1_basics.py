# It will take name and age from user,and print whether user is adult or minor
a = str(input("Enter your name: "))

b = int(input("Enter your age: "))

print("your name is ", a)
print("your age is ", b)

if b >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    
# It will take 2 numbers from user and will print their division
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = a/b

print("The division of two numbers is: ", c)


# we will print data type of each variable
d = 123
e = 12.3
f = "Python"
g = True
h = None

print(f"The type of d is: ", type(d))
print(f"The type of e is: ", type(e))
print(f"The type of f is: ", type(f))
print(f"The type of g is: ", type(g))
print(f"The type of h is: ", type(h))