class Solution(object):
    def isPalindrome(self, s):
        # st2=""
        # for i in s:
        #     if(i>='a' and i<='z' or i>='A' and i<='Z'):
        #         st2+=i.lower()
        #     elif(i>='0' and i<='9'):
        #         st2+=i
        # temp=st2[::-1]
        # if(temp==st2):
        #     return True
        # else:
        #     return False


        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

