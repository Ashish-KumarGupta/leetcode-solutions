from collections import deque
class Solution(object):
    # for dfs
    # def dfs(self, row, col, visited, grid, directions):

    #     n = len(grid)
    #     m = len(grid[0])
    #     visited[row][col] = 1
        
    #     for dx, dy in directions:
    #         nrow = row + dx
    #         ncol = col + dy
    #         if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] ==0 and grid[nrow][ncol] == "O"):
    #             self.dfs(nrow, ncol, visited, grid, directions)





    # for bfs
    def bfs(self, row, col, visited, grid, directions):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        q.append((row, col))
        visited[row][col] = 1
        
        while q:
            r, c = q.popleft()
            for dx, dy in directions:
                nrow = r + dx
                ncol = c + dy
                if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] ==0 and grid[nrow][ncol] == "O"):
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol))
    def solve(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[0]*m for i in range(n)]
        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        
        
        # for row
        for j in range(m):
            # for first row
            if(visited[0][j] == 0 and grid[0][j] == "O"):
                self.bfs(0, j, visited, grid, directions)
                
                
                
            # for last row
            if (visited[n-1][j] == 0 and grid[n-1][j] == "O"):
                self.bfs(n-1, j, visited, grid, directions)
                
                
        # for col
        
        for i in range(n):
            # for first col
            if(visited[i][0] == 0 and grid[i][0] == "O"):
                self.bfs(i, 0,  visited, grid, directions)
                
            # for last col
            if(visited[i][m-1] == 0 and grid[i][m-1] == "O"):
                self.bfs(i, m-1, visited, grid, directions)
                
        # for all others
        for i in range(n):
            for j in range(m):
                if(visited[i][j] == 0 and grid[i][j] == "O"):
                    grid[i][j] = "X"
        return grid
                

        