class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for i in range(len(s)):
            if d[s[i]] ==1:
                return i
        return -1
        

        