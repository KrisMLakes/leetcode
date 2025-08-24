from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        
        ordered = sorted(counts.values(), reverse = True)
        n = len(arr)
        ans, count = 0,0
        for i in ordered:
            if (ans+i) >= n/2:
                ans +=i
                count +=1
                break
            else:
                ans +=i
                count +=1
        return count