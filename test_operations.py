import pytest
from main import suma, resta, multiplicacion, division

def test_suma():
    assert suma(3, 2) == 5
    assert suma(-3, 2) == -1

def test_resta():
    assert resta(5, 2) == 3
    assert resta(-3, -2) == -1

def test_multiplicacion():
    assert multiplicacion(4, 2) == 8
    assert multiplicacion(-3, 2) == -6

def test_division():
    assert division(10, 2) == 5
    assert division(-6, 2) == -3
    with pytest.raises(ValueError):
        division(10, 0)

