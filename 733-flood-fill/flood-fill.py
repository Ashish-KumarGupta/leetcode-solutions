class Solution(object):
    def dfs(self, row, col, image, ans, color, initcolor, direction):

        ans[row][col] = color
        n = len(image)
        m = len(image[0])
        for dx, dy in direction:
            newrow = row + dx
            newcol = col + dy
            if(newrow >= 0 and newrow < n and newcol >= 0 and newcol < m and image[newrow][newcol] == initcolor and ans[newrow][newcol] != color):
                self.dfs(newrow, newcol, image, ans, color, initcolor, direction)




    def floodFill(self, image, sr, sc, color):
        ans = [row[:] for row in image]
        initcolor = image[sr][sc]
        direction = [(-1,0), (0, 1), (1, 0), (0, -1)]
        self.dfs(sr, sc, image, ans, color, initcolor, direction)
        return ans
        