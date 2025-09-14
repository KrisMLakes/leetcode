import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        
        n = len(s)
        print(s)
        for i in range(int(len(s)/2)):
            if s[i] != s[n-1-i]:
                return False
        return True
