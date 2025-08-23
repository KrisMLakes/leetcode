from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            dic[s[right]]= dic[s[right]]+1
            while dic[s[right]]>1:
                dic[s[left]] = dic[s[left]]-1
                left = left +1
            ans = max(ans, right-left+1)
        return ans
            