class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s) #.split("")#.sort()
        t = list(t) #.split("")#.sort()
        print(s, t)
        s.sort()
        t.sort()
        if s == t:
            return True
        else:
            return False
        