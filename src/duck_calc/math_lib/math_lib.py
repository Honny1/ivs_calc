"""@package MathLib

@file math_lib.py
@author Tomas Szabo - xszabo16 - TheRealTom

@brief Library that translates the equations passed from GUI to
       postfix format and solves them
"""

import math
import re


class MathLib():
    def __init__(self):
        """Constructor
        @param self The object pointer
        """
        self.op_stack = []  # The stack for operators
        self.top_index = 0  # Top of stack
        self.output = ""  # The postfix string
        self.precedence = {  # The precendences of each operator
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '_': 3,
            'sin': 3,
            'cos': 3
        }

    def _push(self, element):
        """Pushes value to stack
        @param self The object pointer
        @param element The operator/num passed to op_stack
        """
        self.op_stack.append(element)
        self.top_index += 1

    def _pop(self):
        """Pops value from op_stack
        @param self The object pointer

        @return str|None returns operator when found, otherwise None
        """
        if self.top_index:
            self.top_index -= 1
            return self.op_stack.pop()
        return None

    def _top(self):
        """Returns the top of stack
        @param self The object pointer

        @return str|None returns operator when found, otherwise None
        """
        if self.top_index:
            return self.op_stack[self.top_index - 1]
        return None

    def _not_greater(self, i):
        """Compares two if first not greater
        @param self The object pointer
        @param i Key for the value in precendence directory
        @return bool If the i value is lesser or equal,
                then returns True otherwise False
        @throw KeyError returns None if stack is empty
        """
        try:
            first = self.precedence[i]
            second = self.precedence[self._top()]
            return first <= second
        except KeyError:
            return False

    def _lesser(self, i):
        """Compares two if first lesser
        @param self The object pointer
        @param i Key for the value in precendence directory
        @return bool If the i value is lesser,
                then returns True otherwise false
        @throw KeyError returns None if stack is empty
        """
        try:
            first = self.precedence[i]
            second = self.precedence[self._top()]
            return first < second
        except KeyError:
            return False

    def _stackShouldPop(self, operator):
        """Defines the situation if stack should pop an operation to output
        @param self The object pointer
        @param operator Compared operator
        @return bool if the stack is not empty and
                operator is not greater and "^" or "_"
                or lesser and not "^" or "_" returns True,
                otherwise False
        """
        return self.top_index != 0 \
            and (self._not_greater(operator)
                 and self._left_assoc(operator)
                 or not self._left_assoc(operator)
                 and self._lesser(operator))

    def _load_num(self, input_string, i, len_of_input):
        """Goes through input_string and gets whole number
        @param self The object pointer
        @param input_string Equation in string with or without spaces
        @param i Index of position in input_string in int
        @param len_of_input Length of input_string in int

        @return int|None new index of position in input_string
                         or None when number not suitable
        """
        while input_string[i].isdigit() \
                or input_string[i] == "e" \
                or input_string[i] == ".":
            self.output += input_string[i]

            # Check big number
            if input_string[i] == "e":
                if i + 2 >= len_of_input:
                    return None
                if (input_string[i + 1] != "-"
                        or input_string[i + 1] != "+") \
                        or not input_string[i + 2].isdigit():
                    return None
                self.output += input_string[i + 1]
                i += 2
                continue

            # Check float
            if input_string[i] == ".":
                if i + 1 >= len_of_input or i == 0:
                    return None
                if not input_string[i + 1].isdigit() \
                        and not input_string[i - 1].isdigit():
                    return None

            i += 1

            # Handle end of string
            if i >= len_of_input:
                break
        return i

    def _left_assoc(self, operator):
        """Defines the association when power or root are in a row
        @param self The object pointer
        @param operator The operator in string represantion

        @return bool If operator is neither "^" nor "_", returns True
                      otherwise False
        """
        return operator != "^" and operator != "_"

    def _isNumber(self, str):
        """Checks if number is valid via regex
        @param self The object pointer
        @param str String compared with the regex

        @return re.Match|None If match is found, returns re.Match,
                              otherwise False
        """
        return re.search("^-?[0-9]+(.[0-9]+)?$", str)

    @staticmethod
    def transform_string_to_postfix(input_string):
        """Translate equation input string to postfix
        @param input_string The string of an equation in infix format

        @return str|None Returns postfix format of the input equation
                         or None on wrong format
        """
        stack = MathLib()

        if " " in input_string:
            input_string = input_string.replace(" ", "")
        len_of_input = len(input_string)

        # Iterate input
        i = 0
        while i < len_of_input:
            operator = input_string[i]
            # Num
            if operator.isdigit():
                i = stack._load_num(input_string, i, len_of_input)
                if i is None:
                    return None
                continue
            # Operation
            elif operator == "-":
                if i == 0 or not \
                    stack._isNumber(input_string[i - 1]) and \
                        input_string[i - 1] not in ")(":
                    stack.output += "-"
                    i += 1
                    i = stack._load_num(input_string, i, len_of_input)
                    if i is None:
                        return None
                    continue
                else:
                    # Fill string with operator
                    is_greater = stack._not_greater(operator)
                    if is_greater is None:
                        return None
                    while (stack._stackShouldPop(operator)):
                        stack.output += " " + stack._pop()
                    stack._push(operator)
            # Sin
            elif operator == "s" and i + 5 < len_of_input:
                if not (input_string[i + 1] == "i"
                   and input_string[i + 2] == "n"
                   and input_string[i + 3] == "("):
                    return None
                i = MathLib.evaluate_sin_and_cos(input_string, i, stack, "sin")
                if i is None:
                    return None
            # Cos
            elif operator == "c" and i + 5 < len_of_input:
                if not (input_string[i + 1] == "o"
                   and input_string[i + 2] == "s"
                   and input_string[i + 3] == "("):
                    return None
                i = MathLib.evaluate_sin_and_cos(input_string, i, stack, "cos")
                if i is None:
                    return None
            # Normal operators
            elif operator in "+/*^_":
                # Fill string with operators
                while (stack._stackShouldPop(operator)):
                    stack.output += " " + stack._pop()
                stack._push(operator)
            else:
                return None

            stack.output += " "
            i += 1

        # Empty stack
        if stack.output[len(stack.output) - 1] != " ":
            stack.output += " "
        while stack.top_index != 0:
            stack.output += str(stack._pop()) + " "

        stack.output = re.sub(r'\ (?=\ )', '', stack.output)
        return stack.output[0:-1]

    @staticmethod
    def solve_mathematic_problem(input_string):
        """Translate equation input string to postfix
        @param input_string Infix format of equation in string

        @returns float|None Returns result of the given equation
                          or None when the equation had a bad format
        """
        postfix_string = MathLib.transform_string_to_postfix(input_string)
        if postfix_string is None:
            return None
        return MathLib.solve_postfix_equation(postfix_string)

    @staticmethod
    def solve_postfix_equation(input_postfix):
        """Eval input postfix to number
        @param input_postfix The equation in postfix format in string

        @return float|None Returns float when the equation is solved,
                           otherwise None
        """
        stack = MathLib()
        result = ""

        for element in input_postfix.split():
            if stack._isNumber(element):
                stack._push(element)
            else:
                if element == "sin" or element == "cos":
                    val1 = stack._pop()
                    # Checks None
                    if val1 is None:
                        return None
                    result = str(eval("math." + element + "(" + val1 + ")"))
                elif element in "+/*^_-":
                    val1 = stack._pop()
                    val2 = stack._pop()

                    # Checks None
                    if val1 is None or val2 is None:
                        return None

                    if element == "^":
                        result = str(eval(val2 + "**" + val1))

                    elif element == "_":
                        # root
                        if float(val2) < 0:
                            return None
                        result = str(eval(val2 + "**(1/" + val1 + ")"))

                    else:
                        # Checks dividing by zero
                        if element == "/":
                            if val1 == "0":
                                return None
                            if val2 == "0":
                                stack._push(val2)
                                continue
                        result = str(eval(val2 + element + val1))
                else:
                    return None
                stack._push(result)
        return float(stack._pop())

    @staticmethod
    def evaluate_sin_and_cos(input_string, i, stack, stringType):
        """Makes number from sin and cos
        @param input_string The equation in infix format
        @param i Index of position in input_string
        @param stack The object pointer
        @param stringType "sin" or "cos"

        @return int index of new position in input_string
        """
        in_braces = ""
        another_braces = 0
        result = ""
        i += 4
        len_of_input = len(input_string)
        # Making the infix string in braces
        while i < len_of_input \
            and not (input_string[i] == ")"
                     and another_braces == 0):
            in_braces += input_string[i]
            # Checks braces
            if input_string[i] == "(":
                another_braces += 1
            if input_string[i] == ")":
                another_braces -= 1

            i += 1
        # Solves equation in braces
        result += MathLib.transform_string_to_postfix(in_braces)

        stack.output += str(result) + " " + stringType

        return i
