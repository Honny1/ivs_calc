"""@package MathLib
Documentation of Mathlib

"""
import math

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

    """Compares two """
    def _not_greater(self, i):
        try:
            first = self.precedence[i]
            second = self.precedence[self._top()]
            return first <= second
        except KeyError:
            return None

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
            # Num
            if input_string[i].isdigit():
                i = stack._load_num(input_string, i, len_of_input)
                if i is None:
                    return None
                continue

            # Operation
            operator = input_string[i]
            if operator == "-":
                if i == 0 or not input_string[i-1].isnumeric():
                    stack.output += "-"
                    i += 1
                    i = stack._load_num(input_string, i, len_of_input)
                    if i is None:
                        return None
                    continue
                else:
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
            elif operator in "+\*^_":
                stack._push(operator)
            else:
                return None

            # Fill string with operator
            is_greater = stack._not_greater(operator)
            if is_greater is None:
                return None
            while (not stack.top_index != 0 and stack._not_greater(operator)):
                stack.output += " " + stack._pop()
            
            stack.output += " "
            i += 1

        # Empty stack
        if stack.output[len(stack.output)-1] != " ":
            stack.output += " "
        while stack.top_index != 0:
            stack.output += str(stack._pop()) + " "

        return stack.output[0:-1]

    """Translate equation input string to postfix"""
    @staticmethod
    def solve_mathematic_problem(input_string):
        postfix_string = MathLib.transform_string_to_postfix(input_string)
        if postfix_string == "Invalid Input":
            return "Invalid Input"
        return MathLib.solve_postfix_equation(postfix_string)

    """Eval input postfix to number"""
    @staticmethod
    def solve_postfix_equation(input_postfix):
        stack = MathLib()
        result = ""

        for element in input_postfix.split():
            if element.isnumeric():
                stack._push(element)
            else:
                if element == "sin" or element == "cos":
                    val1 = stack._pop()
                    if val1 is None:
                        return None
                    result = str(eval(element + "(" + val1 + ")"))
                else:       
                    val1 = stack._pop()
                    val2 = stack._pop()

                    if element == "^":
                        result = str(eval(val2 + "**" + val1))
                    elif element == "_":
                        # root
                        result = str(eval(val2 + "**(1/" + val1 + ")"))
                    else:
                        result = str(eval(val2 + element + val1))
                stack._push(result)
        return int(stack._pop())


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


    """Makes number from sin and cos"""
    @staticmethod
    def evaluate_sin_and_cos(input_string, i, stack, stringType):
        in_braces = ""
        result = 0
        i += 4
        len_of_input = len(input_string)
        while i < len_of_input and input_string[i] != ")":
            in_braces += input_string[i]
            i += 1

        try:
            result = eval("math." + stringType + "(" + in_braces + ")")
        except SyntaxError:
            return None

        if i != 0:
            stack.output += " "
        stack.output += str(result)

        return i
