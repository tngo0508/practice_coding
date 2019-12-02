class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in pair:
                close_bracket = c
                open_bracket = stack.pop() if stack else '#'

                if open_bracket != pair[c]:
                    return False
            else:
                stack.append(c)

        return not stack


solution = Solution()
print(solution.isValid('()'))
# True
print(solution.isValid('()[]{}'))
# True
print(solution.isValid('(]'))
# False
print(solution.isValid('([)]'))
# False
print(solution.isValid('((((())))'))
# False
