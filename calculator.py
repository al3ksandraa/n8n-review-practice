def divide(a, b):
    def _coerce_numeric_string(x):
        if isinstance(x, str):
            s = x.strip()
            try:
                return float(s)
            except ValueError:
                # Leave non-numeric strings as-is to preserve original TypeError behavior
                return x
        return x

    a_converted = _coerce_numeric_string(a)
    b_converted = _coerce_numeric_string(b)

    if b_converted == 0:
        raise ValueError("Division by zero")

    return a_converted / b_converted
