class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0,0,1)])
        directions = [(0,1), (1,0),(1,1),(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1)]
        seen={(0,0)}
        n = len(grid)

        def valid(x,y):
            return 0<= x< n and 0<=y<n and grid[x][y] == 0

        while queue:
            x, y, steps = queue.popleft()
            if x == n-1 and y == n-1:
                return steps



            for dx, dy in directions:
                new_row, next_col = x+dx, y+dy
                if valid(new_row, next_col) and (new_row, next_col) not in seen:
                    queue.append((new_row, next_col, steps+1))
                    seen.add((new_row, next_col))
                    

        return -1
        