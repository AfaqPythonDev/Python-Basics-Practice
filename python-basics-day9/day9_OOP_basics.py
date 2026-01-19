'''
Student Class
Create a class named Student
Attributes:
name
age
Method:
display_info() → prints name and age
Create one object and call the method'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

s = Student(name, age)
s.display_info()






'''
Create a class named Calculator
Attributes:
num1
num2
Methods:
add() → prints sum
subtract() → prints difference
Create an object and call both methods'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(f"The sum of {self.num1} and {self.num2} is = {self.num1+self.num2}")
        
    def subtract(self):
        print(f"The difference of {self.num1} and {self.num2} is = {self.num1-self.num2}")
        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

c = Calculator(num1, num2)
c.add()
c.subtract()







'''
Simple Car Class
Create a class named Car
Attributes:
brand
model
Method:
show_details() → prints brand and model
Create an object and display details.'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def show_details(self):
        print(f"The Brand of the car is: {self.brand}")
        print(f"The Model of the car is: {self.model}")
        
brand = input("Brand: ")
model = input("Model: ")

cd = Car(brand, model)
cd.show_details()