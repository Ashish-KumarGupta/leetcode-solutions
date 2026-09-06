from collections import deque
class Solution(object):
    def bfs(self, row, col, visited, grid):
        visited[row][col] = 1
        q = deque()
        q.append((row, col))
        n = len(grid)
        m = len(grid[0])

        while q:
            r,c = q.popleft()

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)
]

            for delrow, delcol in directions:
                nrow = r + delrow
                ncol = c + delcol
                if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] =='1' and visited[nrow][ncol] == 0):
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol))

    def numIslands(self, grid):
        iscnt = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[0]* col for i in range(row)]


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.bfs(i, j, visited, grid)
                    iscnt +=1
        return iscnt