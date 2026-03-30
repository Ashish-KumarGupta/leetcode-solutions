class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        n = len(heights)
        max_area = 0

        right = [n]*n
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            stack.append(i)
        

        stack = []
        left = [-1]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        for i in range(n):
            width = right[i] - left[i] - 1
            current_area = heights[i] * width
            max_area = max(max_area, current_area)
        
        return max_area