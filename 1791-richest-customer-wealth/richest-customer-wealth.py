class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sm = 0
        for i in accounts:
            sm = max(sm, sum(i))
        return sm