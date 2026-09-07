import pytest
from ..app.calculator import add, subtract, divide, multiply

def test_add():
    assert add(10, 10) == 20 # TF-01

    with pytest.raises(TypeError): # TF-02
        add("a", 10)


def test_sub():
    assert subtract(10, 5) == 5 # TF-04

    with pytest.raises(TypeError): # TF-05
        subtract("a", 10)


def test_div():
    assert divide(10, 10) == 1 # TF-07

    with pytest.raises(TypeError): # TF-08
        divide("a", 10)

    with pytest.raises(ZeroDivisionError): # TF-10
        divide(10, 0)


def test_mult():
    assert multiply(10, 10) == 100 # TF-11

    with pytest.raises(TypeError): # TF-12
        subtract("a", 10)


def test_weiteres():
    with pytest.raises(TypeError): # TF-13
        add(10, 10, 10)

    assert add(10, 10) == 20 # TF-14

    with pytest.raises(TypeError): # TF-15
        add(10)

