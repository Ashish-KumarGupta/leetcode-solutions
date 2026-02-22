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