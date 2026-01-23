class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        ans = []
        max_candies = max(candies)
        for i in range(n):
            if (candies[i] + extraCandies) >= max_candies:
                ans.append(True)
            else:
                ans.append(False)

        return ans
