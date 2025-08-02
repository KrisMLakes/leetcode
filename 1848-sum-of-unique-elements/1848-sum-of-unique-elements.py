from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = defaultdict(int)
        for i in nums:
            uniq[i] = uniq[i]+1
        only_once = [uniq1 for uniq1 in uniq if uniq[uniq1]==1] 
        #print (only_once)
        #print(uniq)
        return sum(only_once)

        