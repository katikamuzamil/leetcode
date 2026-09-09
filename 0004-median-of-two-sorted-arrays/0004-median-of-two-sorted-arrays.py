class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num3=sorted(nums1+nums2)
        n=len(num3)
        if len(num3)==1:
            return float(num3[0])  
        elif n%2!=0:
            mid=n//2
            return float(num3[mid])  
        elif len(num3)%2==0:
            n2=len(num3)/2
            ans=(num3[n2]+num3[n2-1])/2.0
            return float(ans)
        
        