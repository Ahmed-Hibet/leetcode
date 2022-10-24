class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        ln = len(nums)
        for i in range(ln):
            if nums[i] == target:
                ans.append(i)
        return ans
        