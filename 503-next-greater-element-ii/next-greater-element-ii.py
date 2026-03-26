class Solution(object):
    def nextGreaterElements(self, nums):
        st=[]
        n= len(nums)
        res=[-1]*n
        for i in range(2*n-1,-1,-1):
            val = nums[i % n]
            

            

            while st and st[-1]<=val:

                st.pop()

                
            if i < n:
                if st:

                        res[i]=st[-1]

          

                    

            st.append(val)

                

        return res