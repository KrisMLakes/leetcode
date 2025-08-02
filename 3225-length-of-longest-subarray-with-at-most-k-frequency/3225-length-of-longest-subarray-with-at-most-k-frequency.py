from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        counts = defaultdict(int)
        for right in range(len(nums)):
            counts[nums[right]]=counts[nums[right]]+1

            while k < counts[nums[right]]:
                counts[nums[left]] = counts[nums[left]] -1
                left = left + 1
            ans = max(ans, right -left+1)
        return ans


        