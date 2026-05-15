def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    else:
        return "Invalid operation"


# Function calls
print("Addition:", calculator(10, 5, "+"))
print("Subtraction:", calculator(10, 5, "-"))
print("Multiplication:", calculator(10, 5, "*"))
print("Division:", calculator(10, 5, "/"))
    