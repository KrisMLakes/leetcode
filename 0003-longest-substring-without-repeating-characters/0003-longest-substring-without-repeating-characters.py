from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            dict[s[right]] = dict[s[right]] + 1
            while dict[s[right]] > 1:
                dict[s[left]] = dict[s[left]] - 1
                left +=1
                

            ans = max(ans, right-left+1)
        return ans