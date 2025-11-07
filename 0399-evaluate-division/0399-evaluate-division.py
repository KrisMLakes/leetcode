from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1/val

        def dfs(src, dest, visited):
            
            if src not in graph or dest not in graph:
                return -1.0
            if src == dest:
                return 1.0
            visited.add(src)
            for nei, val in graph[src].items():
                if nei in visited:
                    continue
                
                res = dfs(nei, dest, visited)
                if res != -1.0:
                    return res*val
            return -1.0







        results = []
        for a, b in queries:
            results.append(dfs(a,b,set()))
        return results

        