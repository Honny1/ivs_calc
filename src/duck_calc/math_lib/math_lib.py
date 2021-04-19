"""@package MathLib
Documentation of Mathlib

"""
import re


class MathLib():
    """Creates stack"""
    def __init__(self):
        self.op_stack = []
        self.top_index = 0
        self.output = ""
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '_': 3,
            'sin': 3,
            'cos': 3
        }

    """Pushes value to stack"""
    def _push(self, element):
        self.op_stack.append(element)
        self.top_index += 1

    """Returns last value"""
    def _pop(self):
        if self.top_index:
            self.top_index -= 1
            return self.op_stack.pop()
        return None

    """Returns the top of stack"""
    def _top(self):
        if self.top_index:
            return self.op_stack[self.top_index-1]
        return None

    """Compares two if first not greater """
    def _not_greater(self, i):
        try:
            first = self.precedence[i]
            second = self.precedence[self._top()]
            return first <= second
        except KeyError:
            return False

    """Compares two if first lesser"""
    def _lesser(self, i):
        try:
            first = self.precedence[i]
            second = self.precedence[self._top()]
            return first < second
        except KeyError:
            return False

    """Clear stack"""
    def _clear_stack(self):
        while self.top_index:
            self._pop()

    """Translate equation input string to postfix"""
    @staticmethod
    def transform_string_to_postfix(input_string):
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
                    MathLib.isNumber(input_string[i-1]) and \
                        input_string[i-1] not in ")(":
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
                    while (MathLib.stackShouldPop(stack, operator)):
                        stack.output += " " + stack._pop()
                    stack._push(operator)
            # Sin
            elif operator == "s":
                i = MathLib.evaluate_sin_and_cos(input_string, i, stack, "sin")
                if i is None:
                    return None
            # Cos
            elif operator == "c":
                i = MathLib.evaluate_sin_and_cos(input_string, i, stack, "cos")
                if i is None:
                    return None
            # Normal operators
            elif operator in "+/*^_":
                # Fill string with operators
                while (MathLib.stackShouldPop(stack, operator)):
                    stack.output += " " + stack._pop()
                stack._push(operator)
            else:
                return None

            stack.output += " "
            i += 1

        # Empty stack
        if stack.output[len(stack.output)-1] != " ":
            stack.output += " "
        while stack.top_index != 0:
            stack.output += str(stack._pop()) + " "

        stack.output = re.sub(r'\ (?=\ )', '', stack.output)
        return stack.output[0:-1]

    """Translate equation input string to postfix"""
    @staticmethod
    def solve_mathematic_problem(input_string):
        postfix_string = MathLib.transform_string_to_postfix(input_string)
        if postfix_string is None:
            return None
        return MathLib.solve_postfix_equation(postfix_string)

    """Eval input postfix to number"""
    @staticmethod
    def solve_postfix_equation(input_postfix):
        stack = MathLib()
        result = ""

        for element in input_postfix.split():
            if MathLib.isNumber(element):
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
                        if float(val2) <= 0:
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

    """Goes through input_string and gets whole number"""
    def _load_num(self, input_string, i, len_of_input):
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

    """Defines the association when pow or root are in a row"""
    def left_assoc(operator):
        return operator != "^" and operator != "_"

    """Checks if number is valid via regex"""
    def isNumber(str):
        return re.search("^-?[0-9]+(.[0-9]+)?$", str)

    """Defines the situation if stack should pop an operation to output"""
    def stackShouldPop(stack, operator):
        return stack.top_index != 0 \
            and (stack._not_greater(operator)
                 and MathLib.left_assoc(operator)
                 or not MathLib.left_assoc(operator)
                 and stack._lesser(operator))

    """Makes number from sin and cos"""
    @staticmethod
    def evaluate_sin_and_cos(input_string, i, stack, stringType):
        in_braces = ""
        another_braces = 0
        result = ""
        i += 4
        len_of_input = len(input_string)
        while i < len_of_input \
            and not (input_string[i] == ")"
                     and another_braces == 0):
            in_braces += input_string[i]
            if input_string[i] == "(":
                another_braces += 1
            if input_string[i] == ")":
                another_braces -= 1
            i += 1
        result += MathLib.transform_string_to_postfix(in_braces)

        # if len(stack.output):
        #    stack.output += " "
        stack.output += str(result) + " " + stringType

        return i
