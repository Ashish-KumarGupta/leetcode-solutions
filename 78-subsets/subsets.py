class Solution(object):
    def helper(self, ind, curr, ans, nums):
        if ind == len(nums):
            ans.append(curr[:])
            return
        curr.append(nums[ind])
        self.helper(ind+1, curr, ans, nums)
        curr.pop()
        self.helper(ind+1, curr,  ans, nums)
    def subsets(self, nums):
        ans = []
        curr = []
        self.helper(0, curr, ans, nums)
        return ans
        
        