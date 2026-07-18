class Solution(object):
    def findsubsets(self, ind, curr, ans, nums):
        ans.append(curr[:])

        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue

            curr.append(nums[i])
            self.findsubsets(i + 1, curr, ans, nums)
            curr.pop()
    def subsetsWithDup(self, nums):
        nums.sort()
        curr = []
        ans = []
        self.findsubsets(0, curr, ans, nums)
        return ans
        