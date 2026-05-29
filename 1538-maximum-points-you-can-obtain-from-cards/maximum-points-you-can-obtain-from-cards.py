class Solution(object):
    def maxScore(self, cardPoints, k):
        lsum = 0
        rsum = 0
        mxsum = 0
        rindex = len(cardPoints)-1

        for i in range(k):
            lsum += cardPoints[i]
            mxsum = lsum

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -=1
            mxsum = max(mxsum, lsum + rsum)
        
        return mxsum
        
        
        
        
        
        
        print(lsum)
        