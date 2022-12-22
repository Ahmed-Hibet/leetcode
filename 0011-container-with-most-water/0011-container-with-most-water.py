class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        right = len(height) - 1
        left = 0
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area: 
                max_area = area
            if height[left] > height[right]: 
                right -= 1
            else: 
                left += 1
        return max_area
