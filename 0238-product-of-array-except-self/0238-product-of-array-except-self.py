class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [nums[-1]]
        total_product = 1
        for num in nums[-2::-1]: 
            answer.append(answer[-1] * num)
        answer.reverse()

        left_product = 1
        n = len(nums)
        for i in range(n):
            right_product = 1
            if i + 1 < n:
                right_product = answer[i+1]
            answer[i] = right_product * left_product
            left_product *= nums[i]
            
        return answer


