# Calculator Function

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operations
print("Addition =", add(num1, num2))
print("Multiplication =", multiply(num1, num2))