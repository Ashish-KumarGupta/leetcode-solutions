class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # ip = address.replace(".", "[.]")
        # return ip

        ans = ""

        for i in address:
            if i == ".":
                ans += "[.]"
            else:
                ans += i
        return ans