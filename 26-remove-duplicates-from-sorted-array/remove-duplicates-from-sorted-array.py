class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # j = 1
        
        # for i in range(len(nums)):
        #     if nums[i] != nums[j-1]:
        #         nums[j] = nums[i]
        #         j +=1
        # return j

        i = 0


        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = temp
                i +=1
        return i+1