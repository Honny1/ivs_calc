import os.path
from duck_calc.math_lib.math_lib import MathLib
import cProfile
import re
def GetSum(list, power):
    resultString = ""
    for i in range(0, len(list)):
        resultString += list[i] + " ^ " + power + " + "
    # delete last operator "+"
    resultString = resultString[:-2]
    return resultString
def GetAritmeticMean(sum, n):
    oneDevidedN = MathLib.solve_mathematic_problem("1 /" + str(n))
    aritMean = MathLib.solve_mathematic_problem(str(oneDevidedN) + "*" + str(sum))
    return str(aritMean)
def GetStandardDeviation():
    listFromFile = []
    if __name__ == "__main__":
        data = input()
        listFromFile = data.split(" ")
    n = len(listFromFile)
    sum = MathLib.solve_mathematic_problem(GetSum(listFromFile, "1"))
    oneDevidedNMinusOne = str(MathLib.solve_mathematic_problem("1 /" + str(n - 1)))
    sumSquared = str(MathLib.solve_mathematic_problem(GetSum(listFromFile, "2")))
    aritMean= str(MathLib.solve_mathematic_problem(GetAritmeticMean(sum, n) + " ^ 1"))
    aritMeanSquared = str(MathLib.solve_mathematic_problem(aritMean + " ^ 2"))
    bracket = str(MathLib.solve_mathematic_problem(sumSquared + " - " + str(n) + " * " + aritMeanSquared))
    underSquareRoot = str(MathLib.solve_mathematic_problem(oneDevidedNMinusOne + " * " + bracket))
    standardDeviation = MathLib.solve_mathematic_problem(underSquareRoot + "_2")

    return standardDeviation


print(GetStandardDeviation())