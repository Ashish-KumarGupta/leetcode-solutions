class Solution(object):
    def isPalindrome(self, s):
        st2=""
        for i in s:
            if(i>='a' and i<='z' or i>='A' and i<='Z'):
                st2+=i.lower()
            elif(i>='0' and i<='9'):
                st2+=i
        temp=st2[::-1]
        if(temp==st2):
            return True
        else:
            return False
        