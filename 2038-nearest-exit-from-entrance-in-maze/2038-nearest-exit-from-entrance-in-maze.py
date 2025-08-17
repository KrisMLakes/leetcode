class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def findexits (maze):

        # Collect exits properly
            for i in range(m):
                if maze[i][0] == ".": 
                    exits.add((i, 0))
                if maze[i][n-1] == ".": 
                    exits.add((i, n-1))
            for j in range(n):
                if maze[0][j] == ".": 
                    exits.add((0, j))
                if maze[m-1][j] == ".": 
                    exits.add((m-1, j))
            return exits
        m = len(maze)
        n = len(maze[0])
        exits = set()
        exits = findexits(maze)
        exits.discard(tuple(entrance))
        queue = deque([(entrance[0],entrance[1], 0)])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = set((entrance[0],entrance[1]))
        steps = 0

        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                if 0<= row+dx < m and 0<= col+dy < n and (row+dx, col+dy) not in seen and maze[row+dx][col+dy] == ".":
                    seen.add((row+dx, col+dy))
                    queue.append((row+dx, col+dy, steps+1))
                    if (row+dx, col+dy) in exits:
                        return steps+1
        return -1



        