class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        dic = {chr(i): 0 for i in range(97, 123)}
        for ch in s1:
            dic[ch] += 1

        total_correct = 0
        for i in range(n1):
            if dic[s2[i]] > 0:
                total_correct += 1
            dic[s2[i]] -= 1
        if total_correct == n1:
            return True
        
        for i in range(n1, n2):
            if dic[s2[i-n1]] >= 0:
                total_correct -= 1
            dic[s2[i-n1]] += 1

            if dic[s2[i]] > 0:
                total_correct += 1
            dic[s2[i]] -= 1

            if total_correct == n1:
                return True
        return False
        
