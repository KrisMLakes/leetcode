from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        
        ordered = sorted(counts.values(), reverse = True)
        n = len(arr)
        ans, count = 0,0
        for i in ordered:
            
            ans +=i
            count +=1
            if ans >= n/2:
                break

        return count