def eval_helper(expression, index=0):
    result = 0
    op = '+'
    while index < len(expression):
        char = expression[index]
        if char.isdigit():
            if op == '+':
                result += int(char)
            else:
                result -= int(char)
        elif char in ('+', '-'):
            op = char
        elif char == '(':
            n, index = eval_helper(expression, index + 1)
            if op == '+':
                result += n
            else:
                result -= n
        elif char == ')':
            return (result, index)
        index += 1
    return (result, index)


def eval(expression):
    return eval_helper(expression)[0]


print eval('- (3 + ( 2 - 1 ) )')
# -4
