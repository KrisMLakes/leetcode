class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        start = [0,0]
        seen.add(tuple(start))
        for i in range(0,len(path)):

            
            if path[i] == "S":
                start[1] = start[1]-1
            elif path[i] == 'N':
                start[1] = start[1]+1
            elif path[i] == 'E':
                start[0] = start[0] + 1
            elif path[i] == 'W':
                start[0] = start[0] - 1
            if tuple(start) in seen:
                return True           
            seen.add(tuple(start))
            #print(seen)

        return False

             
                
        