class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        st = []
        ans = [-1]*n

        for i in range(2*n-1, -1, -1):
            val = nums[i %n]
            while st and val >= st[-1]:
                st.pop()
            if i < n:
                if st:
                    ans[i] = st[-1]
            st.append(val)
        return ans