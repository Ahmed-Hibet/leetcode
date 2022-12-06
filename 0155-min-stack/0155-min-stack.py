class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_level_min = [float('Inf')]
        self.stack_level = 0

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack_level_min) <= self.stack_level + 1:
            self.stack_level_min.append(val)

        if val < self.stack_level_min[self.stack_level]:
            self.stack_level += 1
            self.stack_level_min[self.stack_level] = val
        else:
            self.stack_level += 1
            self.stack_level_min[self.stack_level] = self.stack_level_min[self.stack_level - 1] 

    def pop(self) -> None:
        self.stack.pop()
        self.stack_level -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_level_min[self.stack_level]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
