class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums) #.sort()
        print(nums)
        seeq = {}
        if len(nums)==0:
            return 0
        max_len = 1
        leng = 1
        for i in range(1,len(nums)):

            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                leng +=1 
                max_len = max(max_len, leng) 
            else:
                leng = 1
        return max_len
                    

        