"""@package tests
Test for input string
"""
import pytest

from duck_calc.math_lib.math_lib import MathLib

EPSILON = 0.0001


@pytest.mark.parametrize("problem, result", [
    # sum
    ("1+1", 2),
    ("1 + 1", 2),
    ("69+1", 70),
    ("420+23", 443),
    ("-55+55", 0),
    ("55+-55", 0),
    ("-100+10", -90),
    # sub
    ("1-1", 0),
    ("1 - 1", 0),
    ("69-1", 68),
    ("420-23", 397),
    ("-55-55", -110),
    ("55--55", 110),
    ("-100-10", -110),
    # multi
    ("1*1", 1),
    ("1 * 1", 1),
    ("69*1", 69),
    ("420*23", 9660),
    ("-55*55", -3025),
    ("55*-55", -3025),
    ("-100*10", -1000),
    # div
    ("1/1", 1),
    ("1 / 1", 1),
    ("69/1", 69),
    ("-55/55", -1),
    ("55/-55", -1),
    ("-100/10", -10),
])
def test_solve_problem_with_int_result(problem, result):
    assert MathLib.solve_mathematic_problem(problem) == result


@pytest.mark.parametrize("problem, result", [
    # sum
    ("1+1.1", 2.1),
    ("1 + 1.1", 2.1),
    ("69+1.666", 70.666),
    ("420.999+23.111", 444.11),
    ("-55.1+55.1", 0),
    ("55.1+-55.2", -0.1),
    ("-100.11+-10.9", -111.01),
    # sub
    ("1-1.1", -0.1),
    ("1 - 1.1", -0.1),
    ("69-1.666", 67.334),
    ("420.999-23.111", 397.888),
    ("-55.1-55.1", -110.2),
    ("55.1--55.2", 110.3),
    ("-100.11--10.9", -89.21),
    # multi
    ("1*1.1", 1.1),
    ("1 * 1.1", 1.1),
    ("69*1.666", 114.954),
    ("420.999*23.111", 9729.707889),
    ("-55.1*55.1", -55.1 * 55.1),
    ("55.1*-55.2", -3041.52),
    ("-100.11*-10.9", 1091.199),
    # div
    ("1/1.1", 0.9090909091),
    ("1 / 1.1", 0.9090909091),
    ("69/1.666", 41.41656663),
    ("420.999/23.111", 18.216390463),
    ("-55.1/55.1", -1),
    ("55.1/-55.2", -0.9981884),
    ("-100.11/-10.9", 9.1844036697),
    ("420/23", 18.26086957),
    # power
    ("1^1.1", 1),
    ("1 ^ 1.1", 1),
    ("69^1.666", 1157.504226),
    ("420.999^23.111", 4.464364808341504e+60),
    ("-55.1^55.1", -8.658708053347108e+95),
    ("55.1^-55.2", 7.734491087991536e-97),
    ("-100.11^-10.9", -1.5660141108169798e-22),
    # sqrt
    ("1_1.1", 1),
    ("1_-10", 1),
    ("1 _ 1.1", 1),
    ("555_-10", 0.53158253231947206545914597118368),
    ("69_1.666", 12.69845706),
    ("420.999_23.111", 1.298826584),
    ("55.1_55.1", 1.075473831),
    ("55.1_-55.2", 0.9299452888),
    ("100.11_-10.9", 0.6553449508),
    # sin
    ("sin(1)", 0.8414709848078965),
    ("sin(1) + 1", 1.8414709848078965),
    ("sin(69)", -0.11478481378318722),
    ("sin(420.999)+5", 5.025581627958894924),
    ("sin(55.1)", -0.9925515720731387),
    ("sin(-55.2)", 0.975430723573431),
    ("sin(100.11+10.9)", -0.8695335808328949),
    # cos
    ("cos(1)", 0.5403023058681398),
    ("cos(1) + 1", 1.5403023058681398),
    ("cos(69)", 0.9933903797222716),
    ("cos(420.999)+5", 5.999672736604822),
    ("cos(55.1)", 0.12182518941147201),
    ("cos(-55.2)", 0.2203063855384424),
    ("cos(100.11+10.9)", -0.4938738217438979)
])
def test_solve_problem_with_float_result(problem, result):
    result_of_mathlib = MathLib.solve_mathematic_problem(problem)
    assert (abs(result_of_mathlib) - abs(result)) <= EPSILON


@pytest.mark.parametrize("problem", [
    ("1/0"),
    ("0_1"),
    ("5*(3+0)/0"),
    ("123412/0"),
    ("22+aaa"),
    ("(22+2*2"),
    ("Tohle spocita jen mistr matematiky"),
])
def test_bad_input_values(problem):
    result_of_mathlib = MathLib.solve_mathematic_problem(problem)
    assert result_of_mathlib is None


def test_extream_sum():
    nums = [str(i) for i in range(1, 10000, 3)]
    problem = "+".join(nums)
    result = 16661667
    assert MathLib.solve_mathematic_problem(problem) == result


def test_extream_sub():
    nums = [str(i) for i in range(1, 10000, 3)]
    problem = "-".join(nums)
    result = -16661665
    assert MathLib.solve_mathematic_problem(problem) == result


def test_extream_multi():
    nums = [str(i) for i in range(1, 100, 3)]
    problem = "*".join(nums)
    result = 1745488670154377397414943478973600699284193280000000
    assert abs(MathLib.solve_mathematic_problem(problem) - result) < EPSILON


def test_extream_div():
    nums = [str(i) for i in range(1, 100, 3)]
    problem = "/".join(nums)
    result = 5.7290546601574706e-52
    assert MathLib.solve_mathematic_problem(problem) == result


# def test_extream_power():
#     nums = [str(i) for i in range(1, 200, 3)]
#     problem = "^".join(nums)
#     result = 1
#     assert MathLib.solve_mathematic_problem(problem) == result


# def test_extream_power_1():
#     nums = [str(i) for i in range(5, 8, 1)]
#     problem = "^".join(nums)
#     result = 227373675443232059478759765625
#     assert MathLib.solve_mathematic_problem(problem) == result
