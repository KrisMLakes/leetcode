from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses 

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for nei in graph[course]:
                if not dfs(nei):
                    return False


            visited[course] = 2
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

