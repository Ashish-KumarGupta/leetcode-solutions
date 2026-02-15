class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] +=1
        #     else:
        #         d[i] = 1
        # for i in d:
        #     if d[i] >=2:
        #         return i

        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low
        