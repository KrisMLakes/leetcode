from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        #prefix_sum= defaultdict(int)
        left = 0
        ans = 0
        curr_sum = 0
        #prefix_sum[0]=nums[0]
        for right in range(len(nums)):
            freq[nums[right]]= freq[nums[right]]+1
            curr_sum = curr_sum + nums[right]
           # print(curr_sum, freq)
            #if right >= 1:
            #    prefix_sum[right]= nums[right]+prefix_sum[right-1]
            while freq[nums[right]]>1:
                freq[nums[left]]= freq[nums[left]]-1
                
                curr_sum = curr_sum - nums[left]
                left = left + 1
                #print("while",curr_sum, freq)
            #print(prefix_sum)
            #print(freq)
            ans = max(ans,curr_sum)
        return ans
