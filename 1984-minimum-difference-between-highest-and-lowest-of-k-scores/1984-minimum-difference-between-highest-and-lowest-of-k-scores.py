class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minn = float("Inf")
        ln = len(nums)
        for i in range(ln - k + 1):
            if nums[i+k-1] - nums[i] < minn:
                minn = nums[i+k-1] - nums[i]
        return minn
