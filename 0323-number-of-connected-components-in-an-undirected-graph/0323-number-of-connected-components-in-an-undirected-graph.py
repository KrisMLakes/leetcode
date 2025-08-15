class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)



        seen = set()
        ans = 0

        for i  in range(n):
            if i not in seen:
                ans +=1
                dfs(i)
        return ans
        