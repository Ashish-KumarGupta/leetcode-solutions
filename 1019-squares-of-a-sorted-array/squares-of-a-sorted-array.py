class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            ans.append(i*i)
        ans.sort()
        return ans