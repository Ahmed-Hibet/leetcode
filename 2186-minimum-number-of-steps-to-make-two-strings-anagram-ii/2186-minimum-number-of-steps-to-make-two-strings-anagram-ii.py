class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = {}
        min_step = 0
        for i in s:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        for i in t:
            try:
                dic[i] -= 1
            except:
                dic[i] = -1
        for i in dic.values():
            min_step += abs(i)
        return min_step
