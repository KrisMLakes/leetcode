class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict = {}
        for i in range(len(paths)):
           #print(paths[i][0],paths[i][1])
            dict[paths[i][0]]=paths[i][1]
        
        from1 = set()
        to1 = set()
        from1 = dict.keys()
        to1 = dict.values()
        print(from1)
        print(to1)
        for c in to1:
            if c not in from1:
                return c
        #return set(to1)-set(from1)
        