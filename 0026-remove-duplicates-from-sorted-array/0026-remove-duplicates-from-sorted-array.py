class Solution:
    # 2nd 12/19/25 ( chatgpt)
    # 3rd 1/7/2026  ( partial solve)
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k +=1

                
        return k
 

            
        