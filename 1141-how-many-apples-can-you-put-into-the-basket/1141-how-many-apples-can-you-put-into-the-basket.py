class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        #basketSize = 5000
        ans, i = 0, 0
        for w in weight:
            if (ans+w) > 5000:
                break
            else:
                ans+=w
                i+=1
        return i
            