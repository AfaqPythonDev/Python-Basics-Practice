#Adult or Minor Check
age = int(input("please enter your age: "))

if (age>=18):
    print("you are an adult.")
    print("So you are eligible to vote")
elif (age<=0):
    print("invalid age")
    print("Enter your age again")
else:
    print("You are minor.")
    print("You are not eligible to vote")
    
    
    
    

#Positive, Negative, zero, even, odd
n = int(input("Please enter the number: "))

if (n==0):
    print("you entered the zero, which means nothing")
elif (n>0 and n%2==0):
    print("You entered the postive number")
    print(n, ":is even")
elif (n>0 and n%2!=0):
    print("You entered the postive number")
    print(n, ": is odd")
else:
    print("You entered the negative number")
    
    
    
    

#Greatest of Two Numbers
n1 = int(input("please enter the first number: "))
n2 = int(input("please enter the second number: "))

if (n1>n2):
    print("The greater number is: ", n1)
elif (n2>n1):
    print("The greater number is: ", n2)
else:
    print("Both numbers are equal")
    
    
    
    
#Simple Grade System
marks = int(input("Please enter your marks: "))

if (marks>=90):
    grade = "A"
elif(marks>=80):
    grade = "B"
elif(marks>=70):
    grade = "C"
else:
    grade = "Fail"
    
print("Your grade is: ", grade)
    