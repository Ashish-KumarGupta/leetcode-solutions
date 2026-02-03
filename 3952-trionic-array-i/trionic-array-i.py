class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        i = 0

        
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0:  
            return False

       
        down_start = i
        while i+1 < n and nums[i] > nums[i+1]:
            i += 1
        if i == down_start:  
            return False

        up2_start = i
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == up2_start:  
            return False

        return i == n-1  
