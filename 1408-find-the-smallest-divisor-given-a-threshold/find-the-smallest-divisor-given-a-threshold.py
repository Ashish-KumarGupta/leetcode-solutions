class Solution(object):
    def smallestDivisor(self, nums, threshold):
            
        low = 1
        high = max(nums)

        while(low <= high):

            mid = low + (high - low) //2

            ans = 0
            for i in nums:
                ans += (i + mid - 1) // mid

            if ans > threshold:
                low = mid + 1
            else:
                high = mid -1 
        return low
        