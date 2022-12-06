class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=set()
        for x in range(len(nums1)):
            if(nums1[x] in nums2):
                arr.add(nums1[x])
        return list(arr)
