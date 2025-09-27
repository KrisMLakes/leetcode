class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        op = list("")
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i += 1
            
            end = nums[i]
            print(start, end)
            if start == end:
                op.append(str(start))
            else:
                op.append(f"{start}->{end}")
            i +=1 
        return op
