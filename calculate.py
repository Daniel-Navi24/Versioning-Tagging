def calculate(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    elif operation == 'power':
        return a ** b
    else:
        return "Error: Unsupported operation"

if __name__ == "__main__":
    print(calculate('add', 5, 3))
    print(calculate('power', 2, 3))
