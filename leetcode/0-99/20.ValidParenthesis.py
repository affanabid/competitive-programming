class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        for char in s:
            if char in brackets:
                stack.append(char)
            elif len(stack) == 0 or char != brackets[stack.pop()]:
                return False
        return len(stack) == 0