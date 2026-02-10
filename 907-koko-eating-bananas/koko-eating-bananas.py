class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        result = high

        while(low <= high):
            k = low +(high - low) //2

            hours = 0 

            for p in piles:
                hours += (p+k-1)//k
            if hours <= h:
                result = k
                high = k -1
            else:
                low = k + 1
        return result
        