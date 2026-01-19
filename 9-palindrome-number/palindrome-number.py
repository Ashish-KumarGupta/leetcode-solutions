class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # s = str(x)
        # ans = s[::-1]
        # if s == ans:
        #     return True
        # return False
        

        if (x < 0):
            return False

        rev = 0
        temp = x
        while(x != 0):
            digit = x%10
            rev = (rev * 10) + digit
            x /= 10
        if rev == temp:
            return True
        else:
            return False