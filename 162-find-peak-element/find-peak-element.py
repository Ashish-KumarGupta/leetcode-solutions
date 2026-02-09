class Solution(object):
    def findPeakElement(self, nums):
        first = 0
        last = len(nums) -1

        while(first < last):
            mid = first + (last - first)//2

            if nums[mid] >= nums[mid + 1]:
                last = mid
            else:
                first = mid + 1
        return first

        