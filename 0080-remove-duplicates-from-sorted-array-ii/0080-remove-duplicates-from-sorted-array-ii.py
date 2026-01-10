class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 12/20/25 2nd , chatgpt
        # 1/10/26 3rd
        k, n, j, i = 2, len(nums), len(nums)-1, 2
        #for i in range(2,n-1):
        for i in range(2,n):

            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k +=1
            #i +=1

        return k





