class MyQueue:

    def __init__(self):
        self.read_stack = []
        self.write_stack = []

    def push(self, x: int) -> None:
        self.write_stack.append(x)

    def pop(self) -> int:
        if self.read_stack:
            return self.read_stack.pop()
        while self.write_stack:
            self.read_stack.append(self.write_stack.pop())
        return self.read_stack.pop()

    def peek(self) -> int:
        if self.read_stack:
            return self.read_stack[-1]
        while self.write_stack:
            self.read_stack.append(self.write_stack.pop())
        return self.read_stack[-1]

    def empty(self) -> bool:
        if self.read_stack or self.write_stack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
