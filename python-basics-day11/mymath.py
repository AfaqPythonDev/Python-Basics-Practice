def square(n):
    return n * n

def cube(n):
    return n * n * n


if __name__ == "__main__":
    print("This file is being run directly.")
    
    n = int(input("Enter a number: "))

    print("Square:", square(n))
    print("Cube:", cube(n))

else:
    print("This file is being imported.")

