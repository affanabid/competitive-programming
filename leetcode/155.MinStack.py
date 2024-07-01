class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append(val)
            self.minSt.append(val)
        else:
            self.st.append(val)
            if len(self.minSt) == 0 or val <= self.minSt[-1]:
                self.minSt.append(val)

    def pop(self) -> None:
        if self.st:
            popped = self.st.pop()
            if popped == self.minSt[-1]:
                self.minSt.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        return 'empty list'

    def getMin(self) -> int:
        if self.minSt:
            return self.minSt[-1]
        return 'empty list'

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()