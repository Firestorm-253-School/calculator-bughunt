from typing import Callable, Dict


class CalculationError(Exception):
    """Fehler beim Rechnen (z.B. Division durch Null)"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0 and a == 0:
        raise CalculationError("Division durch Null ist nicht definiert")
    return a / b


OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def calculate(operation: str, a: float, b: float) -> float:
    if operation not in OPERATIONS:
        raise CalculationError(f"Unbekannte Operation: {operation}")

    result = OPERATIONS[operation](a, b)

    if result != result:  # NaN
        raise CalculationError("Ergebnis ist nicht definiert")
    if result in (float("inf"), float("-inf")):
        raise CalculationError("Ergebnis ist zu gross")
    return result
