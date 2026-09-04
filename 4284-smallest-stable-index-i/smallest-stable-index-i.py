class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        maxx = float('-inf')
        minn = float('inf')
        list1 = []
        list2 = [0]*n
        for i in range(n):
            maxx = max(maxx, nums[i])
            list1.append(maxx)
        for i in range(n-1, -1, -1):
            minn = min(minn, nums[i])
            list2[i] = minn
        for i in range(len(list1)):
            if list1[i] - list2[i] <= k:
                return i

        return -1
        