class Solution(object):
    def dfs(self, row, col, image, ans, color, initcolor, direction):

        ans[row][col] = color
        n = len(image)
        m = len(image[0])
        for dx, dy in direction:
            nrow = row + dx
            ncol = col + dy
            if(nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and image[nrow][ncol] == initcolor and ans[nrow][ncol] != color):
                self.dfs(nrow, ncol, image, ans, color, initcolor, direction)




    def floodFill(self, image, sr, sc, color):
        ans = [row[:] for row in image]
        initcolor = image[sr][sc]
        direction = [(-1,0), (0, 1), (1, 0), (0, -1)]
        self.dfs(sr, sc, image, ans, color, initcolor, direction)
        return ans
        