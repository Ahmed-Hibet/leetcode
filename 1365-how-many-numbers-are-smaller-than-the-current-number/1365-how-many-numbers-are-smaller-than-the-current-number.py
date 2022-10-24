class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        ln = len(nums)
        dic = {}
        for i in range(ln - 1, -1, -1):
            dic[temp[i]] = i
        
        solution = []
        for num in nums:
            solution.append(dic[num])
        return solution