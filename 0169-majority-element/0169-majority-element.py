from collections import defaultdict
class Solution:
    # 2nd 12/20/2025   dict example on google
    # 3rd 1/10 dict example lookup
    # in a coding interview, you would be expected to provide the Boyer-Moore solution to achieve constant space
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count +=(1 if candidate==num else -1)
        return candidate
        


        