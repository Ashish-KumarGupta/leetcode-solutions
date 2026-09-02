class Solution(object):
    def uniformArray(self, nums1):
        nums2 = []
        i = nums1[0]
        for j in range(1,len(nums1)):
            nums2.append(i - nums1[j])
        i+=1
        nums2.append(nums1[-1])
        
        for i in range(len(nums2)):
            if nums2[i] % 2 == 0:
                return True
            elif nums2[i] % 2 != 0:
                return True
            else:
                return False
        