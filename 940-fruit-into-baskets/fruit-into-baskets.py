class Solution(object):
    def totalFruit(self, fruits):
        l = 0
        r = 0
        n = len(fruits)
        mpp = {}
        mxlen = 0

        while(r < n):
            if fruits[r] in mpp:
                mpp[fruits[r]] += 1
            else:
                mpp[fruits[r]] = 1

            while(len(mpp) > 2):
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] ==0:
                    del mpp[fruits[l]]
                l +=1
            mxlen = max(mxlen, r - l + 1)

            r +=1
        return mxlen
    
        