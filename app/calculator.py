def add(a, b) -> int:
    return a + b


def dev(a, b) -> float:
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b
