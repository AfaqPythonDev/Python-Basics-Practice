#Create a dictionary with: name, age, department
# Dictionary Basics
dict = {
    "name": "Afaq",
    "age": 21,
    "department": "Software Engineering"
}

print(dict)

print(dict["name"])

dict.update({"Semester" : "7th"})

dict.update({"age": 22})
print(dict)

# Sets Basics
s = {5,3,4,2,6,5,5}
print(s)

s.add(9) # Adding a new element
print(s) 

s.remove(3) # Removing an element
print(s)