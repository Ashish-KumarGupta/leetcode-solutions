class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0

        # DFS


        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
        #         return

        #     grid[r][c] = "0"

        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)

        # BFS

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '0'

            while queue:
                x, y = queue.popleft()

                # 4 directions
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < row and 
                        0 <= ny < col and 
                        grid[nx][ny] == '1'):

                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    # dfs(i, j)
                    bfs(i, j)
                    count +=1
        return count   