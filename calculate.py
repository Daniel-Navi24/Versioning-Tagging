def calculate(operation, operands):
    """Takes a list of operands instead of separate a, b parameters (breaking change)."""
    if operation == 'add':
        return {"status": "ok", "result": sum(operands)}
    elif operation == 'subtract':
        return {"status": "ok", "result": operands[0] - sum(operands[1:])}
    elif operation == 'multiply':
        result = 1
        for n in operands:
            result *= n
        return {"status": "ok", "result": result}
    elif operation == 'divide':
        result = operands[0]
        for n in operands[1:]:
            if n == 0:
                return {"status": "error", "message": "Cannot divide by zero"}
            result /= n
        return {"status": "ok", "result": result}
    else:
        return {"status": "error", "message": "Unsupported operation"}

if __name__ == "__main__":
    print(calculate('add', [5, 3]))
