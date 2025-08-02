class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = sorted(list(s1))
        len1 = len(s1)
        print(len1, arr1)
        for i in range(len(s2)):
            #print(i,s2[i])
            if s2[i]  in arr1:
               # print(s2[i], s2[i:i+len1])
                if s2[i:i+len1] is not None:
                    if arr1 == sorted(list(s2[i:i+len1])):
                        return True
        return False
               # if i+1 is not null and s2[i+1] is in arr1:
                    
        