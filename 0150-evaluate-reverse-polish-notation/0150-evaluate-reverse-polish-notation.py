class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                a = stack.pop()
                stack[-1] = str(int(eval(stack[-1] + i + a)))
        return int(stack[-1])
