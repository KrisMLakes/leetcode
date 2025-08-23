from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        for i in list(ransomNote):
            dic[i] = dic[i] + 1
        for j in list(magazine):
            dic2[j] = dic2[j] + 1
        
        arr = dic.keys()
        arr2 = dic2.keys()
        print (dic)
        print (dic2)
        for k in arr:
            if ((dic2[k] is None) or (dic[k] > dic2[k])):
                #print (dic[k])
                return False
            #else:
        return True
            
            
        