class Solution(object):
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
                if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] ==0 and grid[nrow][ncol] == 1):
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol))
    def numEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        visited = [[0]*m for i in range(n)]
        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        
        
        # for row
        for j in range(m):
            # for first row
            if(visited[0][j] == 0 and grid[0][j] == 1):
                self.bfs(0, j, visited, grid, directions)
                
                
                
            # for last row
            if (visited[n-1][j] == 0 and grid[n-1][j] == 1):
                self.bfs(n-1, j, visited, grid, directions)
                
                
        # for col
        
        for i in range(n):
            # for first col
            if(visited[i][0] == 0 and grid[i][0] == 1):
                self.bfs(i, 0,  visited, grid, directions)
                
            # for last col
            if(visited[i][m-1] == 0 and grid[i][m-1] == 1):
                self.bfs(i, m-1, visited, grid, directions)
                
        # for all others
        cnt = 0
        for i in range(n):
            for j in range(m):
                if(visited[i][j] == 0 and grid[i][j] == 1):
                    cnt += 1
        return cnt




# from collections import deque
# class Solution(object):
#     def numEnclaves(self, grid):
#         n = len(grid)
#         m = len(grid[0])
#         q = deque()

#         visited = [[0]*m for _ in range(n)]

#         for i in range(n):
#             for j in range(m):
#                 # for row and column of all boundaries 
#                 if(i == 0 or j == 0 or i == n-1 or j == m-1):
#                     if(grid[i][j] == 1):
#                         q.append((i, j))
#                         visited[i][j] = 1


#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#         while q:
#             r, c, = q.popleft()

#             for dx, dy in directions:
#                 nrow = r + dx
#                 ncol = c + dy
#                 if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
#                     q.append((nrow, ncol))
#                     visited[nrow][ncol] = 1
#         count = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1 and visited[i][j] ==0:
#                     count += 1
#         return count