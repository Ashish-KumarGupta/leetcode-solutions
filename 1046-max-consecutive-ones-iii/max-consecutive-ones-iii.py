class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        l = 0
        r = 0
        zero = 0
        mxlen = 0
        while(r < n):
            if(nums[r] == 0):
                zero +=1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l +=1

            mxlen = max(mxlen, r-l +1)
            r += 1
        return mxlen