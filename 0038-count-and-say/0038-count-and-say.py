class Solution:
    s = '1'
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return self.s
        current = self.s[0]
        count = 1
        temp_s = ''
        ln = len(self.s)
        for i in range(1, ln):
            if self.s[i] == current:
                count += 1
            else:
                temp_s += str(count) + current
                current = self.s[i]
                count = 1
        temp_s += str(count) + current
        self.s = temp_s
        return self.countAndSay(n - 1)
        
    