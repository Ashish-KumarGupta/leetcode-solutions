class Solution(object):
    def findCombination(self, ind, target, candidates, curr, ans):
        if ind == len(candidates):
            if target == 0:
                ans.append(curr[:])
            return
        if candidates[ind] <= target:
            curr.append(candidates[ind])
            self.findCombination(ind, target - candidates[ind], candidates, curr, ans)
            curr.pop()

        self.findCombination(ind+1, target, candidates, curr, ans)


    def combinationSum(self, candidates, target):
        curr = []
        ans = []
        self.findCombination(0, target, candidates, curr, ans)
        return ans 
        
        