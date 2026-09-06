from typing import Protocol


class CalculationLogger(Protocol):
    def log(self, operation: str, a: float, b: float, result: float) -> None: ...


class NoopLogger:
    def log(self, operation: str, a: float, b: float, result: float) -> None:
        return None


class ConsoleLogger:
    def log(self, operation: str, a: float, b: float, result: float) -> None:
        print(f"[calc] {operation}({a}, {b}) = {result}")
