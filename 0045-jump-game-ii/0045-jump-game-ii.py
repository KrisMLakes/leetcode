class Solution:
    def jump(self, nums: List[int]) -> int:
# 2nd 1/21/26, saw solution
        current_end, jumps, max_reach = 0, 0, 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i+nums[i])
            if current_end == i:
                jumps +=1
                current_end = max_reach
        return jumps

