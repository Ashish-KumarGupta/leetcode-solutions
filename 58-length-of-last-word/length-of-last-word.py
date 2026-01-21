class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.split()
        # temp=[]
        # for i in l:
        #     if(i!=''):
        #         temp.append(i)
        # return len(temp[-1])
        ans = len(l) -1
        return len(l[ans])
        