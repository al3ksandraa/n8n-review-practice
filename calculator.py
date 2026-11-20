def divide(a, b):
    # Convert numeric strings to numbers; preserve behavior for numeric inputs
    if isinstance(a, str):
        a_converted = float(a.strip())
    else:
        a_converted = a

    if isinstance(b, str):
        b_converted = float(b.strip())
    else:
        b_converted = b

    if b_converted == 0:
        raise ValueError("Division by zero")

    return a_converted / b_converted
