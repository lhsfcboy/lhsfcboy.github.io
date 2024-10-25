#! /usr/bin/env python
#  coding:utf8

import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, r", [(9, 8, 17), (7, 6, 13), (5, 4, 9), (3, 2, 5), (1, 0, 1)])
def test_add(calc, a, b, r):
    assert calc.add(a, b) == r

@pytest.mark.parametrize("a, b, r", [(9, 8, 1), (7, 6, 1), (5, 4, 1), (3, 2, 1), (1, 0, 1)])
def test_sub(calc, a, b, r):
    assert calc.sub(a, b) == r

@pytest.mark.parametrize("a, b, r", [(9, 8, 72), (7, 6, 42), (5, 4, 20), (3, 2, 6), (1, 0, 0)])
def test_mul(calc, a, b, r):
    assert calc.mul(a, b) == r

@pytest.mark.parametrize("a, b, r", [(9, 3, 3), (8, 4, 2), (6, 2, 3), (4, 2, 2), (0, 1, 0)])
def test_div(calc, a, b, r):
    assert calc.div(a, b) == r

def test_div_error(calc):
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)
