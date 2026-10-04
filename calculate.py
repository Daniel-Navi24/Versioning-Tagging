def calculate(operation, operands):
    if not isinstance(operands, list):
        return {"status": "error", "message": "Operands must be a list"}
    if len(operands) < 2:
        return {"status": "error", "message": "At least two operands required"}
    for n in operands:
        if not isinstance(n, (int, float)):
            return {"status": "error", "message": "All operands must be numbers"}

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
    elif operation == 'modulo':
        if operands[1] == 0:
            return {"status": "error", "message": "Cannot modulo by zero"}
        return {"status": "ok", "result": operands[0] % operands[1]}
    else:
        return {"status": "error", "message": "Unsupported operation"}

if __name__ == "__main__":
    print(calculate('add', [5, 3]))
    print(calculate('add', 'bad'))
