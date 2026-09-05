class Solution(object):
    def firstStableIndex(self, nums, k):
        mx = float('-inf')
        mn = float('inf')
        l1 = []
        l2 = [0]*len(nums)

        for i in range(len(nums)):
            mx = max(mx, nums[i])
            l1.append(mx)
        
        for i in range(len(nums)-1, -1,-1):
            mn = min(mn, nums[i])
            l2[i] = mn
        
        
        for i in range(len(l1)):
            if l1[i] - l2[i] <= k:
                return i
        return -1