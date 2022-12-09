class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ln = len(nums)
        left = [0 for i in range(ln)]
        right = [0 for i in range(ln)]

        sum_left = 0
        sum_right = 0
        for i in range(ln):
            left[i] = sum_left
            sum_left += nums[i]

            right[ln - 1 - i] = sum_right
            sum_right += nums[ln -1 - i]
        
        for i in range(ln):
            if left[i] == right[i]:
                return i
        return -1

