class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = float('inf')
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        
        while right < len(nums) and left < len(nums):
            if (nums[right] - (nums[left-1] if left>0 else 0 )) >= target:
                #print (nums[right], nums[left], target, right, left)
                ans = min(ans, right-left+1)
                #print(ans)
                left = left + 1
            else:
                #print (nums[right], nums[left], target, right, left)
                right = right + 1
        #print (nums)
        return ans if ans != float('inf') else 0