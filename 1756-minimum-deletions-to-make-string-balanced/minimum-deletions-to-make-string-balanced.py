class Solution(object):
    def minimumDeletions(self, s):
        b = 0
        a = 0
        for i in s:
            if i == 'b':
                b +=1
            else:
                a = min(a +1, b)
        return a
        
        