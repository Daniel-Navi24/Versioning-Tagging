def calculate(operation, a, b):
    """Returns a dict with result and status (breaking change from number return)."""
    if operation == 'add':
        return {"status": "ok", "result": a + b}
    elif operation == 'subtract':
        return {"status": "ok", "result": a - b}
    elif operation == 'multiply':
        return {"status": "ok", "result": a * b}
    elif operation == 'divide':
        if b == 0:
            return {"status": "error", "message": "Cannot divide by zero"}
        return {"status": "ok", "result": a / b}
    elif operation == 'power':
        return {"status": "ok", "result": a ** b}
    else:
        return {"status": "error", "message": "Unsupported operation"}

if __name__ == "__main__":
    print(calculate('add', 5, 3))
