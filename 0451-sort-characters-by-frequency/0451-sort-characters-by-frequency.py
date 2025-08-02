from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        arr = list(s)
        s1=''
        #print(arr)
        for j in arr:
            #print(j)
            #print (freq[j])
            freq[j]=freq[j]+1
        arr1 = sorted(freq.values(), reverse=True)
        #print(arr1)
        while  arr1:# is not None:
            j = arr1[0]
            #print(j)
            for k in list(freq):
                if freq[k]==j:
                    s1 = s1 + k*j
                    #print(freq[k],k)
                    del freq[k]
            #print(arr1)
            arr1.remove(j)
        return s1
        