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
    else:
        return "Error: Unsupported operation"

if __name__ == "__main__":
    print(calculate('add', 5, 3))
    print(calculate('subtract', 5, 3))
    print(calculate('multiply', 5, 3))
    print(calculate('divide', 5, 3))
    print(calculate('divide', 5, 0))
