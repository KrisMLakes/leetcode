
from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        if m == 0:
            return s2 == s3
        if n == 0: 
            return s1==s3
        
        @cache
        def dp(i,j,k):
            if i == m and j ==n:
                return True

            ans = False
            if i < m and s1[i] == s3[k]:
                ans = ans or dp(i+1,j,k+1)
            if j < n and s2[j] == s3[k]:
                ans = ans or dp(i,j+1,k+1)
            
            return ans



        return dp(0, 0, 0)