class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right =  0, n-1
        max_area = 0

        while left < right:
            max_area = max(max_area, min(height[left],height[right])*(right - left))
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_area
