class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for x in range(len(nums1)):
            if(nums1[x] in nums2):
                arr.append(nums1[x])
                nums2.remove(nums1[x])
        return arr
