from app.calculator import calculate, CalculationError
import pytest;

def test_addition():
    assert calculate("add", 1_000_000_000_000, 1) == 1_000_000_000_001


def test_subtraction():
    assert calculate("subtract", -1_000_000_000_000, 1) == -1_000_000_000_001


def test_multiplication():
    assert calculate("multiply", 20, 10) == 200

def test_division_by_zero():
    with pytest.raises(CalculationError, match="Division durch Null ist nicht definiert"):
        calculate("divide", 10, 0)


def test_number_too_small():
    with pytest.raises(ValueError):
        calculate("add", -1_000_000_000_001, 1)


def test_number_too_large():
    with pytest.raises(ValueError):
        calculate("add", 1_000_000_000_001, 1)


def test_unknown_operation():
    with pytest.raises(
        CalculationError,
        match="Unbekannte Operation: safsafa"
    ):
        calculate("safsafa", 1, 1)

def test_non_numeric():
    with pytest.raises(ValueError, match="Operands must be numeric"):
        calculate("add", "abc", "")
        