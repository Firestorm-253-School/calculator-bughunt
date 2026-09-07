from .calculator import CalculationError, calculate
from .logger import CalculationLogger, NoopLogger

MAX_ABS_INPUT = 1e12


class CalculatorService:
    def __init__(self, logger: CalculationLogger | None = None) -> None:
        self._logger = logger or NoopLogger()

        self.history = []

    def perform(self, operation: str, a: float, b: float) -> float:

        result = calculate(operation, a, b)
        self._logger.log(operation, a, b, result)
        return result

    def append_history(self, entry: tuple[str, float, float, float]) -> None:
        pass
