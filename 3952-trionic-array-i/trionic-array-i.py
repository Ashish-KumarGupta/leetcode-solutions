class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        i = 0


        # up
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0:
            return False

        # down
        dn_start = i
        while i+1 < n and nums[i] > nums[i+1]:
            i +=1
        if i == dn_start:
            return False
        # again up
        up_again = i
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == up_again:
            return False
        return i == n-1
