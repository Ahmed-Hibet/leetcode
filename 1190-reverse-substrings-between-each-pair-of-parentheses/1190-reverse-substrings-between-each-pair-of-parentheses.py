class Solution:
    def __init__(self):
        self.stack = []

    def reverseParentheses(self, s: str) -> str:
        for i in s:
            if i == ')':
                rev = ''
                while self.stack[-1] != '(':
                    rev += self.stack.pop()
                self.stack.pop()
                for j in rev:
                    self.stack.append(j)
            else:
                self.stack.append(i)
        result = ''
        while self.stack:
            result = self.stack.pop() + result

        return result
      
