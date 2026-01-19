'''
Person → Student
Create class Person
name
age
Create class Student (inherits Person)
roll_number
Method to display all details'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        
    def show_details(self):
        print(f"The name of the Person is: {self.name}")
        print(f"The age of the Person is: {self.age}")
        print(f"The Roll No of the Person is: {self.roll_number}")
        
        
name = input("Enter name: ")
age = int(input("Enter age: "))
roll = int(input("Enter roll number: "))

s = Student(name, age, roll)
s.show_details()





'''
Vehicle → Car
Create class Vehicle
brand
Create class Car (inherits Vehicle)
model
Method to show vehicle info'''


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
        
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
    def vehicle_Info(self):
        print("        ----Car Details----               ")
        print(f"The Brand of the Vehicle is: {self.brand}")
        print(f"The Model of the Vehicle is: {self.model}")

brand = input("Brand: ")
model = input("Model: ")
        
b = Car(brand, model)
b.vehicle_Info()
       
       
       
       
       



'''
Animal → Dog
Create class Animal
name
Create class Dog (inherits Animal)
Override a method to display sound'''

class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):   # Overriding method
        print(f"{self.name} says: Woof! Woof!")

c = Dog("Jack")
c.sound()

