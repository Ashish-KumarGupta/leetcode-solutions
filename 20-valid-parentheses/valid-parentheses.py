class Solution(object):
    def isValid(self, s):
        # stack = []
        # mapp = {'}':'{', ']':'[', ')':"("}

        # for char in s:
        #     if char in mapp:
        #         # if not stack:
        #         #     return False
        #         # last = stack.pop()
        #         # if mapp[char] != last:
        #         #     return False

        #         if not stack or stack[-1] != mapp[char]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(char)
        # return len(stack) == 0



        stack = []
        for i in range(len(s)):
            if s[i] =='(' or s[i] =='[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                
                if s[i] ==')' and top!='(' or s[i] =='}' and top!='{' or s[i] ==']' and top!='[':
                    return False
               
        return len(stack)==0

