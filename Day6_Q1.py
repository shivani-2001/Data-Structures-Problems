# Question - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if (len(self.min_stack) == 0) or (self.min_stack[-1] >= val):
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop(-1)
        if val == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()