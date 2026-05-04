class Solution(object):

    def dfs(self, row, col, ans, image, color, delrow, delcol, initcolor):
    
        ans[row][col] = color  

        n = len(image)
        m = len(image[0])

        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]

            if (0 <= nrow < n and 0 <= ncol < m and 
                image[nrow][ncol] == initcolor and 
                ans[nrow][ncol] != color):

                self.dfs(nrow, ncol, ans, image, color, delrow, delcol, initcolor)

    def floodFill(self, image, sr, sc, color,):
        initcolor = image[sr][sc]
        ans = []
        for row in image:
            ans.append(row[:])

        delrow = [-1, 0, +1, 0]
        delcol = [0, +1, 0, -1]
        self.dfs(sr, sc, ans, image, color, delrow, delcol, initcolor)
    
        return ans