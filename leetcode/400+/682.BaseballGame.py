class Solution:
    def is_number(self, string):
        return string.strip('-').isdigit() and string.strip() != ''

    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            op = operations[i]
            if self.is_number(op):
                stack.append(int(op))
            elif op == '+':
                sm = stack[-1] + stack[-2]
                stack.append(sm)
            elif op == 'D':
                d = 2 * stack[-1]
                stack.append(d)
            elif op == 'C':
                stack.pop() 
        
        return sum(stack)
