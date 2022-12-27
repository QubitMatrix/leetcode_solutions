class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(m)
        for x in range(len(nums2)):
            for y in range(len(nums1)):
                if(nums2[x]<nums1[y] or y>=m):
                    nums1[y+1:]=nums1[y:-1]
                    nums1[y]=nums2[x]
                    m+=1
                    print(nums1)
                    break
