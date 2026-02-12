class Solution(object):
    def bs(self, arr,target):


            low=0
            high=len(arr)-1


            while low<=high:


                mid=(low+high)//2


                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return False

    def searchMatrix(self, matrix, target):


        

        m=len(matrix)


        for i in range(m):
            if matrix[i][0]<=target<=matrix[i][-1]:
                return self.bs(matrix[i],target)
        return False
        
