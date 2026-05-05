class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()
        vis = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))     #row , col, time
                elif grid[i][j] == 1:
                    vis += 1

        time = 0

        drow = [-1, 0, +1, 0]
        dcol = [0, +1, 0, -1]

        while q:
            r, c, t = q.popleft()
            time = max(time , t)

            for i in range(4):
                nr = r + drow[i]
                nc = c + dcol[i]

                if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    vis -= 1
                    q.append((nr, nc, t+1))

        if vis == 0:
            return time
        else:
            return -1
