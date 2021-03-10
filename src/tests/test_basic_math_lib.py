"""Tests of math lib example
"""
from duck_calc.math_lib.math_lib import ExampleMathLib


def test_example_test_sum():
    """ test docstring """
    assert ExampleMathLib.sum_a_b(1, 2) == 3


def test_example_test_odd():
    """ test docstring """
    assert ExampleMathLib.odd_a_b(1, 2) == -1
