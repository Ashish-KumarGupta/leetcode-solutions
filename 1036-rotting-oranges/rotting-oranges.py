from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                    visited[i][j] = 2
        tm = 0 
        directions = [(-1,0), (0,1),(1,0),(0,-1)]

        while q:
            r,c,t = q.popleft()
            tm = max(tm, t)
            for dx, dy in directions:
                newrow = r + dx
                newcol = c + dy
                if(newrow >= 0 and newrow < n and newcol >= 0 and newcol < m and visited[newrow][newcol] == 0 and grid[newrow][newcol] == 1):
                    q.append((newrow, newcol, t+1))
                    visited[newrow][newcol] = 1

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1 and visited[i][j] == 0:
                    return -1

        return tm       