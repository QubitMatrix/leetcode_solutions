class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)
        s3=s1 & s2
        return min(s3) if s3 else -1
