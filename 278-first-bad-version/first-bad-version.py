# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        ans = -1
        while(low <= high):
            mid = low + (high - low) //2

            if isBadVersion(mid) == True:
                ans =  mid
                high = mid - 1
            else:
                low = mid + 1

        return ans