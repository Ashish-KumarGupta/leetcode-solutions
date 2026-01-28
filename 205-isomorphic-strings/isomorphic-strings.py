class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # map_st = {}
        # map_ts = {}

        # for i in range(len(s)):
        #     if s[i] in map_st:
        #         if map_st[s[i]] != t[i]:
        #             return False
        #     else:
        #         if t[i] in map_ts:
        #             return False
        #         map_st[s[i]] = t[i]
        #         map_ts[t[i]] = s[i]

        # print(map_st[s[i]])

        # return True

        dic1 =[]
        dic2 = []

        for i in s:
            dic1.append(s.index(i))

        for i in t:
            dic2.append(t.index(i))
        return dic1 == dic2