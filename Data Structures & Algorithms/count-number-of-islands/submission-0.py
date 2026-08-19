from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use BFS traversal [0,1], [0,-1],[-1,0],[1,0] direction
        # count when queue empty, record visited node (x,y)
        dirs = [[0,1], [0,-1],[-1,0],[1,0]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(i, j):
            queue = deque([[i, j]])
            while queue:
                m, n = queue.popleft()
                visited.add((m, n))
                for x, y in dirs:
                    mx, ny = m+x, n+y 
                    if 0 <= mx < rows and 0 <= ny < cols and (mx, ny) not in visited and grid[mx][ny] == "1":
                        visited.add((mx, ny))
                        queue.append([mx, ny])

            return

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count

            
            
