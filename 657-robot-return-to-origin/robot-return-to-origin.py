class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        left = moves.count("L")
        right = moves.count("R")
        up = moves.count("U")
        dn = moves.count("D")

        if left == right and up == dn:
            return True
        else:
            return False