#print numbers
n = int(input("How many numbers you want to print: "))
for i in range(1, n+1):
    print(i)
    





#Sum of First N Numbers

n = int(input("Please enter the number: "))

i = 1
sum = 0
while (i<=n):
    sum = sum+i
    i = i+1
print("The sum of numbers are: ", sum)




#Multiplication Table
n = int(input("Please enter the number: "))

i = 1

while(i<=10):
    print(f"{n} * {i} = {n*i}")
    i = i+1
    
    
    
    

#Count Characters
s = str(input("Please write something: "))

count = 0

for i in s:
    count = count + 1

print("Number of characters:", count)



#factorial

n = int(input("Please enter the number: "))

i = 1

product = 1

while(i<=n):
    product = product * i
    i = i + 1
print("The factorial of",n, "is = ", product)