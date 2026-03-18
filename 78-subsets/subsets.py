class Solution(object):
    def solve(self, nums, res, temp, start):
        if start == len(nums):
            res.append(temp[:])
            return

        # include
        temp.append(nums[start])
        self.solve(nums, res, temp, start+1)

        # exclude
        temp.pop()
        self.solve(nums, res, temp, start+1)

    def subsets(self, nums):
        res = []
        temp = []

        self.solve(nums, res, temp, 0)
        return res


        