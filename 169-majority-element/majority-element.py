class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # for i in d :
        #     if d[i] > len(nums)//2:
        #         return i
        

        nums.sort()

        return nums[len(nums)/2]
        