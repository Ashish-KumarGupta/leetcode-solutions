class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        l=0
        r=0
        mxlen = 0
        zeros = 0

        while(r < n):
            if nums[r] == 0:
                zeros +=1
            while (zeros > k):
                if (nums[l] == 0):
                    zeros -=1
                l +=1
            if (zeros <= k):
                mxlen = max(mxlen, r - l + 1)
            r +=1
        return mxlen
