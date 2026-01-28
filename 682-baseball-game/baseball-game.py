class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        l = []

        for i in operations:
            if i == "D":
                prev = l[-1]
                l.append(prev*2)
            elif i == "C":
                l.pop()
            elif i == "+":
                last = l[-1]
                second_last = l[-2]
                l.append(last + second_last)
            else:
                l.append(int(i))
        return sum(l)
