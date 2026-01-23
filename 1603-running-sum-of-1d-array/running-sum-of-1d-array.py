class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sm = 0
        for i in range(len(nums)):
            sm = sm + nums[i]
            ans.append(sm)
        return ans