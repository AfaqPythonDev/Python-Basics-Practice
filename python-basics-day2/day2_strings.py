# String Basics
name = str(input("Enter any word(At least 6 characters): "))
print("The word is:", name) # Output the entered word

print("The length of the word is:", len(name)) # Output the length of the word

print("The first character is:", name[0]) # Output the first character of the word

print("The last character is:", name[-1]) 


# String Operations
print("This is the Upper case:", name.upper()) # Convert all characters to uppercase

print("This is the Lower case: ", name.lower()) # Convert all characters to lowercase

print("This is the Title case: ", name.title()) # Convert the first character of each word to uppercase

print("Replace the word: ", name.replace(name[2], "e")) # Replace the third character with 'e'



# String Slicing
print("The first 5 characters are: ", name[0:5]) # Output the first 5 characters of the word
print("The last 5 Characters are: ", name[-5:]) # Output the last 5 characters of the word