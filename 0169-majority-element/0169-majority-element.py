from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1
        k = len(nums)
        for num in nums:
            if counts[num] >= k/2:
                return num
        #return
 

        