def calculation_helper(stack):
    print stack
    res = stack.pop() if stack else 0
    # print res
    while stack and stack[-1] != ')':
        sign = stack.pop()
        # print sign
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res


def calculation(s):
    stack = []
    n, operand = 0, 0
    for i in range(len(s) - 1, -1, -1):
        # print stack
        ch = s[i]
        # print ch
        if ch.isdigit():
            operand = operand + (10 ** n * int(ch))
            n += 1
        elif ch != ' ':
            if n:
                stack.append(operand)
                n, operand = 0, 0
            elif ch == '(':
                res = stack.calculation_helper(stack)
                stack.pop()
                stack.append(res)
            else:
                print ch
                stack.append(ch)
                # print stack
    if n:
        stack.append(operand)
    return calculation_helper(stack)


print calculation_helper('(7-(8+9))')
# print calculation('- (300 + ( 200 - 100 ) )')
# -4
