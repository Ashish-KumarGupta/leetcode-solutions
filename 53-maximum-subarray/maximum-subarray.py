class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms = float('-inf')
        cs = 0
        # for i in range(len(nums)):
        #     cs = max(nums[i] , cs + nums[i])
        #     ms = max(cs, ms)
        # return ms
        for n in nums:
            if cs < 0:
                cs = 0

            cs += n
            ms = max(ms, cs)
        
        return ms

