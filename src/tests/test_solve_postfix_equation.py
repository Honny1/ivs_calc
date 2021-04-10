"""
Test Postfix evaluation
"""
from duck_calc.math_lib.math_lib import MathLib
import pytest


@pytest.mark.parametrize("problem, result", [
    ("1 1 +", 2),
    ("11 9 +", 20),
    ("583 12 +", 595),
    ("-1 1 +", 0),
    ("-126 26 +", -100),
    ("987654321 123456789 +", 1111111110),
    ("-987654321 123456789 +", -864197532),

    ("1 1 -", 0),
    ("29 9 -", 20),
    ("583 33 -", 550),
    ("1 1 -", 0),
    ("-126 24 -", -150),
    ("987654321 123456789 -", 864197532),
    ("-987654321 123456789 -", -1111111110),

    ("1 0 *", 0),
    ("3 3 *", 9),
    ("120 20", 2400),
    ("-1 1 *", 0),
    ("5 -6 *", -30),
    ("9876543 123456 *", 451149483006),
    ("-987654 123456 *", -451149483006),

    ("0 1 /", 0),
    ("20 4 /", 5),
    ("1266 3 /", 422),
    ("0 -1 /", 0),
    ("-1266 3 /", -422),
    ("987654322 2 -", 493827161),
    ("-987654322 2 -", -493827161)
])

def test_postfix_conversion(problem, result):
    assert MathLib.solve_mathematic_problem(problem) == result


@pytest.mark.parametrize("problem", [
    ("velký špatný"),
    ("1 0 /"),
    ("-1 0 /"),
    ("0 1 + +"),
    ("0 1 / /"),
    ("55sadf 2 /"),
    ("54fa 2 *"),
    ("87aef7 +"),
    ("-78sf885 2 -")
])

def test_bad_input(problem):
    result_of_mathlib = MathLib.solve_mathematic_problem(problem)
    assert result_of_mathlib is None
