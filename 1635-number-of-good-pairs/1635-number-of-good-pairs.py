from collections import defaultdict
import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        dict1 = defaultdict(int)
        for j in nums:
            dict1[j]= dict1[j]+1
        print(dict1)
        for j in dict1.values():
            if j > 1:
                ans = ans + int(j*(j-1)/2)
        return ans


        