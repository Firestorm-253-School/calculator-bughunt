from .calculator import CalculationError, calculate
from .logger import CalculationLogger, NoopLogger

MAX_ABS_INPUT = 1e12


class CalculatorService:
    def __init__(self, logger: CalculationLogger | None = None) -> None:
        self._logger = logger or NoopLogger()

    def perform(self, operation: str, a: float, b: float) -> float:

        result = calculate(operation, a, b)
        self._logger.log(operation, a, b, result)
        return result

