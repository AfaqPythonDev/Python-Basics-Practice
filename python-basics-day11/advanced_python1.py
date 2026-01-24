import mymath

num = int(input("Enter a number: "))

print("Square:", mymath.square(num))
print("Cube:", mymath.cube(num))



from mymath import square

num2 = 7
result = square(num2)

print("Square (from import):", result)



import math

print("\nAll functions inside math module:")
print(dir(math))