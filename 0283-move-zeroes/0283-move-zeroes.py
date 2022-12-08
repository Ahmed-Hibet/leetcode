class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        non_zero_index = 0
        zero_index = 0
        flag = False
        while non_zero_index < ln:
            if nums[non_zero_index] != 0:
                if flag:
                    nums[non_zero_index], nums[zero_index] = nums[zero_index], nums[non_zero_index]
                    zero_index += 1
            elif not flag:
                flag = True
                zero_index = non_zero_index
            non_zero_index += 1
            


                
