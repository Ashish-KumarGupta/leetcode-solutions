class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        l = 0
        r = 0
        mxlen = 0
        mapp = {}
        while (r<n):
            if s[r] in mapp:
                if mapp[s[r]] >= l:
                    l = mapp[s[r]] + 1
            mxlen = max(mxlen, r - l +1)
            mapp[s[r]] = r
            r +=1
        return mxlen

    

        # mapp = {} 
        # l = 0
        # r = 0
        # n = len(s)
        # maxLen = 0

        # while r < n:

        #     if s[r] in mapp and mapp[s[r]] >= l:
        #         l = mapp[s[r]] + 1

        #     mapp[s[r]] = r
        #     maxLen = max(maxLen, r - l + 1)

        #     r += 1

        # return maxLen
