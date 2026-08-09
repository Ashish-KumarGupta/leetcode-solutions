class Solution(object):
    def findcombination(self, ind, target, candidates, ans, curr):
        if(target == 0):
            ans.append(curr[:])
            return
        for i in range(ind, len(candidates)):
            if(i > ind and candidates[i] == candidates[i-1]):
                continue
            if(candidates[i] > target):
                break
            curr.append(candidates[i])
            self.findcombination(i+1, target - candidates[i], candidates, ans, curr)
            curr.pop()

    def combinationSum2(self, candidates, target):
        
        candidates.sort()
        ans = []
        curr = []
        self.findcombination(0, target, candidates, ans, curr)
        return ans