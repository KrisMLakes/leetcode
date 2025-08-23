class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums)-1
        #print (num[j])
        for i in range(0,len(nums)-1):
            while j > i:
                if (nums[i]+nums[j] == target):
                    return [i,j]
                j=j-1
            j=len(nums)-1


        