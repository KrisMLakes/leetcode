class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        def dfs(node):
            ans = 1
            
            for i in list(graph[node]):
                if i not in restricted and i not in seen:
                    seen.add(i)
                    ans += dfs(i)
            return ans
                
        graph = defaultdict(list)
        seen = set()
        #ans = 0
        restricted = set(restricted)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        
        if 0 in restricted:
            return 0
        seen.add(0)
        
        return dfs(0)
        