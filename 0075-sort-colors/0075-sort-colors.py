class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        ln = len(nums)
        index = 0
        for i in range(ln):
            while not count[index]:
                index += 1
            nums[i] = index
            count[index] -= 1