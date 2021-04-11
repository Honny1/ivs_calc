def string_to_postfix(string):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '_': 3, '^': 3}
    stack = []
    numbers = []
    postfix = ""
    for char in string:
        if char in precedence:
            numbers.append(" ")
            postfix += " "

            for i, operand in enumerate(stack):
                if precedence[operand] > precedence[char]:
                    numbers.append(stack[i])
                    numbers.append(" ")
                    stack.pop(i)

            for i, operand in enumerate(stack):
                if precedence[operand] == precedence[char]:
                    numbers.append(stack[i])
                    numbers.append(" ")
                    stack.pop(i)

            stack.append(char)
            noDuplic = []
            for i in stack:
                if i not in noDuplic:
                    noDuplic.append(i)
                else:
                    numbers.append(i)

            stack = noDuplic

        elif char.isdigit() or char.isalpha():
            numbers.append(char)

    for i, operand in enumerate(stack):
        for j, oper in enumerate(stack):
            if precedence[operand] > precedence[oper]:
                numbers.append(" ")
                numbers.append(stack[i])
                numbers.append(" ")
                stack.pop(i)
    if len(stack) == 1:
        numbers.append(stack[0])
        stack.pop(0)

    postfix = ''.join(numbers)
    return postfix