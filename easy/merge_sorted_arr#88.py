class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        y=0
        for x in range(len(nums1)):
            if(y<len(nums2) and nums1[x]>nums2[y]):
                for z in range(len(nums1)-2,x-1,-1):
                    nums1[z+1]=nums1[z]
                nums1[x]=nums2[y]
                y+=1
            if(x-y==m and nums1[x]==0):
                for z in range(x,len(nums1)):
                    nums1[z]=nums2[y]
                    y+=1
                break
