a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
def exp(a, b):
    return a ** b
add
subtract
multiply
divide
exp
print(f"The sum of {a} and {b} is: {add(a, b)}")
print(f"The difference of {a} and {b} is: {subtract(a, b)}")
print(f"The product of {a} and {b} is: {multiply(a, b)}")
print(f"The quotient of {a} and {b} is: {divide(a, b)}")
print(f"{a} raised to the power of {b} is: {exp(a, b)}")