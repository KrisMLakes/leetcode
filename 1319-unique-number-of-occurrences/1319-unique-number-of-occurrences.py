from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for i in arr:
            freq[i]=freq[i]+1
        if len(freq.values()) > len(set(freq.values())):
            return False
        else:
            return True