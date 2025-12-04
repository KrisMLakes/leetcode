class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]*(n*n+1)
        label = 1

        for row in range(n-1, -1, -1):
            if (n-1-row)%2 == 0:
                for col in range(n):
                    arr[label] = board[row][col]
                    label +=1



            else:
                for col in range(n-1,-1,-1):
                    arr[label] = board[row][col]
                    label +=1
        dist = [-1]*(n*n+1)
        q = deque([1])
        dist[1] = 0

        while q:
            current_cell = q.popleft()
            if current_cell == n*n:
                return dist[current_cell]
            
            for dice_roll in range(1,7):
                next_cell = current_cell + dice_roll
                if next_cell <= n*n:
                    if arr[next_cell] != -1:
                        destination = arr[next_cell]
                    else:
                        destination = next_cell
                    
                    if dist[destination] == -1:
                        dist[destination] = dist[current_cell]+1
                        q.append(destination)
        return -1


        

        