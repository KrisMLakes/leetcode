from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = 0
        ans = 0
        curren = 0
        
        pre_count = defaultdict(int)
        pre_count[0]=1
        for right in range(len(nums)):
            curren = curren + nums[right]
            ans = ans + pre_count[curren-goal]
            pre_count[curren] = pre_count[curren]+1
            
        return ans
        