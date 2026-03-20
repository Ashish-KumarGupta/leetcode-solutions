class Solution(object):
    def isValid(self, s):
        stack = []
        mapp = {'}':'{', ']':'[', ')':"("}

        for char in s:
            if char in mapp:
                # if not stack:
                #     return False
                # last = stack.pop()
                # if mapp[char] != last:
                #     return False

                if not stack or stack[-1] != mapp[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

