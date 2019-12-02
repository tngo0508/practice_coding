class Solution:
    def isValid(self, s):
        open_paren = ['(', '[', '{']
        close_paren = [')', ']', '}']
        stack = []

        for char in s:
            if char in open_paren:
                stack.append(char)
            elif char in close_paren:
                if not stack:
                    return False
                if open_paren.index(stack.pop()) != close_paren.index(char):
                    return False
        return not stack


s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
