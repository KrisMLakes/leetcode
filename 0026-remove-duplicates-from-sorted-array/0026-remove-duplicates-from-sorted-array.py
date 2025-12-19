class Solution:
    # 2nd 12/19/25
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k = 1, 1, len(nums)

        for j in range(1, len(nums)):
            if nums[j] > nums[j-1]:
                nums[i] = nums[j]
                i +=1
        return i
            

            
        