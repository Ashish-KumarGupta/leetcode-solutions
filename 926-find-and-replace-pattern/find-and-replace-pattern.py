class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isMatch(word, pattern):
            map_p_w = {}
            map_w_p = {}

            for i in range(len(word)):
                p = pattern[i]
                w = word[i]

                if p in map_p_w:
                    if map_p_w[p] != w:
                        return False
                else:
                    if w in map_w_p:
                        return False
                    map_p_w[p] = w
                    map_w_p[w] = p
            return True

        res = []
        for word in words:
            if isMatch(word, pattern):
                res.append(word)
        return res