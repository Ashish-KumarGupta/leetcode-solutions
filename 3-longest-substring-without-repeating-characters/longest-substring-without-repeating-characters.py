class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapp = {}
        l = 0
        mxlen = 0

        for r in range(len(s)):

            if s[r] in mapp and mapp[s[r]] >= l:
                l = mapp[s[r]] + 1

            mxlen = max(mxlen, r - l + 1)

            mapp[s[r]] = r

        return mxlen