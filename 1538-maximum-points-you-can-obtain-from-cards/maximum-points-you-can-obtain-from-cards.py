class Solution(object):
    def maxScore(self, cardPoints, k):
        leftSum = 0
        rightsum = 0 
        maxsum = 0
        n = cardPoints

        for i in range(k):
            leftSum += n[i]
            maxsum = leftSum

        rindex = len(n) - 1
        for i in range(k-1, -1 , -1):
            leftSum -= n[i]
            rightsum += n[rindex]
            rindex -= 1
            maxsum = max(maxsum, leftSum + rightsum)
        return maxsum
        
