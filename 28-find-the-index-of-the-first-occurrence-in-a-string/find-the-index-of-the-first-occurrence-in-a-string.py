class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle in haystack:
        #     return haystack.index(needle)
        # return -1


        # return haystack.find(needle)

        for i in range((len(haystack)- len(needle)+1)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
