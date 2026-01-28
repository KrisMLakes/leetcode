class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums)-1
        for i in range(len(nums)):
            while j > i:
                if nums[i] + nums[j] == target:
                    return [i,j]
                j -=1
            j = len(nums)-1
        

        