class Solution(object):
    # def findsubsets(self, ind, curr, ans, nums):
    #     ans.append(curr[:])

    #     for i in range(ind, len(nums)):
    #         if i > ind and nums[i] == nums[i - 1]:
    #             continue

    #         curr.append(nums[i])
    #         self.findsubsets(i + 1, curr, ans, nums)
    #         curr.pop()
    # def subsetsWithDup(self, nums):
    #     nums.sort()
    #     curr = []
    #     ans = []
    #     self.findsubsets(0, curr, ans, nums)
    #     return ans
        

    def helper(self, ind, curr, ans, nums):
        if ind >=len(nums):
            ans.append(curr[:])
            return
        curr.append(nums[ind])
        self.helper(ind + 1, curr, ans, nums)
        curr.pop()
        while (ind +1 < len(nums)) and (nums[ind] == nums[ind + 1]):
            ind += 1
        self.helper(ind + 1, curr, ans, nums)

    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        curr = []
        self.helper(0, curr, ans, nums)
        return ans