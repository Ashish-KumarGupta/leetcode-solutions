class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[1:] = sorted(nums[1:])
        # return (nums[0] + nums[1] + nums[2])


        min1 = float('inf')
        min2 = float('inf')

        for i in nums[1:]:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i

        return nums[0] + min1 + min2

        


