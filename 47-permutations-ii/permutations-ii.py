class Solution(object):
    def getper(self, curr, ans, mapp, nums):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        for i in range(len(nums)):
            if i not in mapp:
                if i>0 and nums[i] == nums[i-1] and (i-1) not in mapp:
                    continue
                curr.append(nums[i])
                mapp[i] = 1
                self.getper(curr, ans, mapp, nums)
                del mapp[i]
                curr.pop()
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        curr = []
        mapp = {}
        self.getper(curr, ans, mapp, nums)
        return ans
        
        