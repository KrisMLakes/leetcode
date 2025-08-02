from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr1 = []
        freq = defaultdict(int)
        for i in arr:
            freq[i]= freq[i]+1
        lucky = -1
        for j in freq:
            if freq[j] == j:
                arr1.append(j)

        if len(arr1) == 0:
            return -1
        else:
            return max(arr1)
        #if not [freq[j] for j in freq if freq[j]==j]: # is None:
        #    return -1
       # else:
        #    return max([freq[j] for j in freq if freq[j]==j])

        #lucky = (if [freq[j] for j in freq if freq[j]==j] is None -1 else max[freq[j] for j in freq if freq[j]==j])

        #return lucky        