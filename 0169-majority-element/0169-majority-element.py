from collections import defaultdict
class Solution:
    # 2nd 12/20/2025   dict example on google
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums)
        major_dict = {}
        for i in nums:
            if i in major_dict:

                major_dict[i] = major_dict[i] + 1
            else:
                major_dict[i] = 1
                
            if major_dict[i] > count/2:
                return i
        


        