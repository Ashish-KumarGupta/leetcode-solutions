class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[1:] = sorted(nums[1:])
        return (nums[0] + nums[1] + nums[2])
        