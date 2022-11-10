class Solution:
    def binarySearch(self, nums: List[int], target: int, currentIndex: int) -> int:
        _min = 0
        _max = len(nums) - 1
        while _min <= _max:
            md = (_min + _max)//2
            value = nums[md][0]
            if value == target:
                return nums[md][1]
            elif value > target:
                _max = md - 1
            else:
                _min = md + 1
        return currentIndex
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            nums[i] = (nums[i], i)
        nums.sort()
        for i in range(ln):
            req = target - nums[i][0]
            nums[i] = (req + 1, nums[i][1])
            result = self.binarySearch(nums, req, nums[i][1])
            if result != nums[i][1]:
                return [result, nums[i][1]]
            nums[i] = (target - req, nums[i][1])
            
            