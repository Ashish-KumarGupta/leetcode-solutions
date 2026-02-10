class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1


        while(low <= high):
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid +1
            else:
                high = mid - 1
        return low
        