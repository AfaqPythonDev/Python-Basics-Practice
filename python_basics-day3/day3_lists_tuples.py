#List Basics
list = [63, 83, 92, 4, 7]
print("This is the list: ", list) #prints full list

print(list[0]) #prints first element of the list

print(list[-1]) #prints last element of the list

print(len(list)) #prints length of the list


# List Operations
list.append(45)
print(list) #prints list after appending 45

list.remove(83)
print(list) #prints list after removing 83

list.sort()
print("This is the updated list: ", list) #prints sorted list

# Tuple Basics
tuple = (63, 83, 92, 4, 7)
print("This is the tuple: ", tuple) #prints full tuple

print(tuple[0]) #prints first element of the tuple
print(tuple[-1])
print(len(tuple))

# tuple[0] = 100  # This will raise an error since tuples are immutable
# #This shows that tuples cannot be modified after creation