class Solution(object):
    def repermutation(self, ans, curr, mapp, nums):
        if(len(curr) == len(nums)):
            ans.append(curr[:])
            return
        for i in range(len(nums)):
            if i not in mapp:
                curr.append(nums[i])
                mapp[i] = 1
                self.repermutation(ans, curr, mapp, nums)
                del mapp[i]
                curr.pop()
    def permute(self, nums):
        ans = []
        curr = []
        mapp = {}
        self.repermutation(ans, curr, mapp, nums)
        return ans
        